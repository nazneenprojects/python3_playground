"""
The struct module provides pack() and unpack() functions for working with variable length binary record formats.
The following example shows how to loop through header information in a ZIP file without using the zipfile module.
Pack codes "H" and "I" represent two and four byte unsigned numbers respectively.
The "<" indicates that they are standard size and in little-endian byte order:
"""

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()
    print(data.__sizeof__())


start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
