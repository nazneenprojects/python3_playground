import zlib
from zipfile import crc32

s = b'which which has which witchers wrist watch'
print(s, len(s))
t = zlib.compress(s)
print(t, len(t))
a = zlib.decompress(t)
print(a)

print(zlib.crc32(s))