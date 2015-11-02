import struct

infile=open('bubble24.png','rb')
png_header=infile.read(100)
png_magic = struct.unpack('8s', png_header[0:8])[0]
png_width = struct.unpack('>I', png_header[16:20])[0]
png_height = struct.unpack('>I', png_header[20:24])[0]
png_depth = struct.unpack('B', png_header[24:25])[0]

print("png magic: " + str(png_magic))
print("png width: " + str(png_width))
print("png height:" + str(png_height))
print("png depth:" + str(png_depth))


#  > big-endian standard none 
# 小端转换,png图片数据是用Big-Endian存储数值数据的需要转换为大端模式。
# png是大端格式存储的
# http://www.360doc.com/content/11/0428/12/1016783_112894280.shtml
# http://blog.csdn.net/blues1021/article/details/45007943