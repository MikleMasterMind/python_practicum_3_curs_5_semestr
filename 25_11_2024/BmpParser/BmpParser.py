import sys
import struct
import io


data = sys.stdin.buffer.read()
f = io.BytesIO(data)

header = struct.unpack("<2s", f.read(2))[0]
if header != b"BM":
    print("Not a Windows BMP")
    exit()
    
size = struct.unpack("<I", f.read(4))[0]
f.read(8)
if len(data) != size:
    print("Incorrect size")
    exit()

dib_size = struct.unpack("<I", f.read(4))[0]
if dib_size not in {12, 16, 40, 52, 56, 64, 108, 124}:
    print("Incorrect header size")
    exit()

dib = f.read(dib_size - 4)
if dib_size in {12, 16}:
    width, height, levels, bits = struct.unpack("<HHHH", dib[:8])
    comp, bung = 0, 0
else:
    width, height, levels, bits, comp, image_size = struct.unpack("<iiHHII", dib[:20])
    row = (width * bits + 31) // 32 * 4
    image_size_new = row * abs(height)
    flag = image_size == 0 or image_size == image_size_new or image_size == image_size_new + 2
    bung = image_size - image_size_new if flag else 0
    if not flag:
        print("Incorrect image size")
        exit()
print(f"{abs(width)} {abs(height)} {bits} {comp} {bung}")
