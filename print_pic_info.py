#!/usr/bin/python
#
import struct

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
	
infile = open('test1.gif', 'rb')
gif_header = infile.read(100)
print_gif(gif_header);
print('')

infile = open('test16.bmp', 'rb')
bmp_header = infile.read(100)
print_bmp(bmp_header);
print('')

infile = open('bubble24.png', 'rb')
png_header = infile.read(100)
print_png(png_header);