import struct

infile = open('test2.gif', 'rb')
gif_header = infile.read(10)
gif_magic = struct.unpack('6s', gif_header[0:6])[0]
gif_width = struct.unpack('H', gif_header[6:8])[0]
gif_height = struct.unpack('H', gif_header[8:10])[0]

print("gif magic: " + str(gif_magic))
print("gif width: " + str(gif_width))
print("gif height:" + str(gif_height))

# reference
# _https://docs.python.org/2/library/struct.html
# _http://www.lightbird.net/py-by-example/struct-module.html
# _https://pymotw.com/2/struct/
# http://vislab-ccom.unh.edu/~schwehr/rt/python-binary-files.html
# _http://stackoverflow.com/questions/18977978/python-parsing-data-from-binary-file-using-structs
# _http://blog.csdn.net/wzy198852/article/details/17266507
