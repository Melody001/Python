import struct

infile = open('boy.bmp', 'rb')
bmp_header = infile.read(54)
bmp_magic = struct.unpack('2s', bmp_header[0:2])[0]
bmp_width = struct.unpack('I', bmp_header[18:22])[0]
bmp_height = struct.unpack('I', bmp_header[22:26])[0]

print("bmp magic: " + str(bmp_magic))
print("bmp width: " + str(bmp_width))
print("bmp height:" + str(bmp_height))

# reference
#bmp的资料:
#_http://blog.csdn.net/lanbing510/article/details/8176231 
#_http://www.fastgraph.com/help/bmp_header_format.html
# _https://docs.python.org/2/library/struct.html
# _http://www.lightbird.net/py-by-example/struct-module.html
# _https://pymotw.com/2/struct/
# _http://vislab-ccom.unh.edu/~schwehr/rt/python-binary-files.html
# _http://stackoverflow.com/questions/18977978/python-parsing-data-from-binary-file-using-structs
# _http://blog.csdn.net/wzy198852/article/details/17266507
#_ https://docs.python.org/2/library/struct.html#struct.unpack_from
