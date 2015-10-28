import struct

infile = open('boy.bmp', 'rb')
bmp_header = infile.read(54)
bmp_magic = struct.unpack('2s', bmp_header[0:2])[0]
bmp_width = struct.unpack('I', bmp_header[18:22])[0]
bmp_height = struct.unpack('I', bmp_header[22:26])[0]

print("bmp magic: " + str(bmp_magic))
print("bmp width: " + str(bmp_width))
print("bmp height:" + str(bmp_height))