import asyncio
import sys


class FilterQueue(asyncio.Queue):
    
    def __init__(self, maxsize=0):
        super().__init__(maxsize)
        
    @property
    def window(self):
        return self._queue[0]
    
    def __contains__(self, filter):
        return any(filter(i) for i in self._queue)
    
    def later(self):
        if super().empty():
            raise asyncio.QueueEmpty
        
        elem = super().get_nowait()
        super().put_nowait(elem)
        
    async def get(self, filter=None):
        if not filter or not self.__contains__(filter):
            elem = await super().get()
        else:
            elem = await super().get()
            while not filter(elem):
                await super().put(elem)
                elem = await super().get()
        return elem


exec(sys.stdin.read())