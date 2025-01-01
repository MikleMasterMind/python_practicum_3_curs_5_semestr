import asyncio
import sys


class Monster:
    def __init__(self, name, position, delay, power):
        self._name = name
        self._position = position
        self._delay = delay
        self._power = power
        self._alive = True
        self._n = 0
    
    async def run(self, start_episod: asyncio.Barrier, end_episod: asyncio.Barrier):
        while True:        
            await start_episod.wait()
            self._n += 1
            if self.alive() and self._delay == self._n:
                self._position += 1
                self._n = 0
            await end_episod.wait()
    
    def alive(self):
        return self._alive
    
    def kill(self):
        self._alive = False
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, *args):
        self._power = sum(args)
        
    def __str__(self):
        return self._name
    
    def position(self):
        return self._position
    
    
    
async def game(monsters: list[Monster], start_episod: asyncio.Barrier, end_episod: asyncio.Barrier, epoch):
    count_epoch = 0
    while any(m.alive() for m in monsters) and count_epoch < epoch:
        await start_episod.wait()
        await end_episod.wait()
        count_epoch += 1
        
        monsters_alive = monsters_alive = [m for m in monsters if m.alive()]
        if len(monsters_alive) == 1:
            break
        
        
        points = {}
        monster1, monster2 = None, None
        for monster in sorted(monsters_alive, key=lambda m: m.position()):
            if monster.position() in points:
                points[monster.position()].append(monster)
            else:
                points[monster.position()] = [monster]
            if len(points[monster.position()]) == 2:
                monster1 = points[monster.position()][0]
                monster2 = points[monster.position()][1]
                break

        if monster1 and monster2:
            if monster1.power == monster2.power:
                monster1.kill()
                monster2.kill()
            else:
                strong_monster = monster1 if monster1.power > monster2.power else monster2
                weak_monster = monster1 if monster1.power < monster2.power else monster2
                strong_monster.power -= weak_monster.power
                weak_monster.kill()
        
        await asyncio.sleep(0)
    
    monsters_alive = [m for m in monsters if m.alive()]
    
    if len(monsters_alive) == len(monsters):
        return 'All flee'
    elif monsters_alive:
        return ', '.join(str(m) for m in monsters_alive)
    else:
        return 'All dead'
                
                
exec(sys.stdin.read())