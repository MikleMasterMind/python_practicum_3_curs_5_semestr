import sys
import tarfile
import io

archive = ''.join(sys.stdin.read().split())
binary_data = bytes.fromhex(archive)
with tarfile.open(fileobj=io.BytesIO(binary_data), mode='r') as tar:
    size = sum(i.size for i in tar.getmembers() if i.isfile())
    files = sum(1 for i in tar.getmembers() if i.isfile())
    print(size, files)
