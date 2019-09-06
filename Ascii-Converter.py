import sys
import argparse
import math
import numpy
from PIL import Image as ImagePIL
from colorama import init
from colorama import Fore, Style

# Initialize colorama
init()

# 10 levels of grays
grays = " %/\\*+=-:."

args = argparse.ArgumentParser(description="This Python script converts an image into ASCII art")
args.add_argument('--f', dest='infile', required=True)
args.add_argument('--r', dest='resolution', required=False)
args.add_argument('--s', dest='scale', required=False)
args.add_argument('--o', dest='outfile', required=False)
args = args.parse_args()

# Input image file
infile = args.infile

# Output filename
outfile = 'ascii.txt'
if args.outfile:
	outfile = args.outfile + '.txt'

# Height of ASCII image
resolution = 100
if args.resolution:
	resolution = int(args.resolution)

# Width/height, default to 0.43 since it's a good value for ASCII art in Courier font
scale = 0.43
if args.scale:
	scale = int(args.scale)

print(Fore.CYAN + "\nASCII Converter\n" + Fore.MAGENTA + "Made by github.com/raghavverma2\n" + Style.RESET_ALL)

image = ImagePIL.open(infile).convert('L')
print(Fore.YELLOW + "Image dimensions =\t" + Fore.CYAN + str(image.size[0]) + " x " + str(image.size[1]) + " pixels")

# Width and height of each ASCII tile
width = image.size[0]/resolution
height = width/scale

# Width of ASCII image
rows = int(image.size[1]/height)

print(Fore.YELLOW + "ASCII dimensions =\t" + Fore.CYAN + str(resolution) + " x " + str(rows) + " characters")

# If image is less than resolution
if resolution > image.size[0] or rows > image.size[1]:
	print(Fore.RED + "Specified resolution too large for image")
	exit(1)

# Image array is list of ASCII strings
img = []

for i in range(rows):

	# Correct final tile
	if i == rows - 1:
		y2 = image.size[1]
	img.append("")

	for j in range(resolution):

		if j == resolution - 1:
			x2 = image.size[0]

		# Coordinates of tile
		tile = image.crop((int(j * width), int(i * height), int((j + 1) * width), int((i + 1) * height)))
		npImg = numpy.array(tile)
		imgW, imgH = npImg.shape
		luminance = numpy.average(npImg.reshape(imgW * imgH))

		# Average luminance of tile
		avgArr = int((luminance*9)/255)

		try:
			# Append character to ASCII string
			img[i] += grays[avgArr]
		except IndexError:
			print(Fore.RED + "\nERROR: This shouldn't happen")
			exit(1)

# Open and write each row to specified file
f = open(outfile, 'w')

for row in img:
	f.write(row + '\n')

f.close()
print(Fore.YELLOW + "\nASCII art written to\t" + Fore.CYAN + outfile)