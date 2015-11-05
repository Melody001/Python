#!/usr/bin/python
#
import struct
import sys

def print_gif(gif_header):
	print("magic is: " + str(struct.unpack('6s', gif_header[0:6])[0]))
	print("width is: " + str(struct.unpack('H', gif_header[6:8])[0]))
	print("height is: " + str(struct.unpack('H', gif_header[8:10])[0]))
	return;

def print_bmp(bmp_header):
	print("magic is: " + str(struct.unpack('2s', bmp_header[0:2])[0]))
	print("width is: " + str(struct.unpack('I', bmp_header[18:22])[0]))
	print("height is: " + str(struct.unpack('I', bmp_header[22:26])[0]))
	print("depth is: " + str(struct.unpack('H', bmp_header[28:30])[0]))
	return;
	
def print_png(png_header):
	print("magic is: " + str(struct.unpack('8s', png_header[0:8])[0]))
	print("width is: " + str(struct.unpack('>I', png_header[16:20])[0]))
	print("height is: " + str(struct.unpack('>I', png_header[20:24])[0]))
	print("depth is: " + str(struct.unpack('B', png_header[24:25])[0]))
	return;

def check_pic_type(pic_header):
	ret_type = "unknown"
	pic_type = struct.unpack('1B', pic_header[0:1])[0]
	#print(pic_type)
	if (pic_type == 0x47):  # gif
		ret_type = 'gif'
	elif (pic_type == 0x42): # bmp
		ret_type = 'bmp'
	elif (pic_type == 0x89): # png
		ret_type = 'png'
	#print(ret_type)
	return ret_type;

#print(str(len(sys.argv)))
if(len(sys.argv) != 2):
	print('Please input file name');
	exit()

infile = open(sys.argv[1], 'rb')
pic_header = infile.read(100)
pic_type = check_pic_type(pic_header)
if pic_type == 'gif':
	print_gif(pic_header);
elif pic_type == 'bmp':
	print_bmp(pic_header)
elif pic_type == 'png':
	print_png(pic_header)
else:
	print('Unkonwon file')
print('')


#infile = open(sys.ardayv[2], 'rb')
#bmp_header = infile.read(100)
#print_bmp(bmp_header);
#print('')

#infile = open(sys.argv[3], 'rb')
#png_header = infile.read(100)
#print_png(png_header);

#print ("script name: " + sys.argv[0])
#print("pic name: " + sys.argv[1])