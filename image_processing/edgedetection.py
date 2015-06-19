# -*- coding:utf-8 -*-
import Image
import math

def edgedetection(imagefile):
	image = Image.open(imagefile)
	outputimage = Image.new( "RGB", (image.size[0], image.size[1]) )

	"""set Gx and Gy"""
	Gx = [
		[-1, 0, 1],
		[-2, 0, 2],
		[-1, 0, 1]
	]
	Gy = [
		[-1, -2, -1],
		[0, 0, 0],
		[1, 2, 1]
	]

	for i in range(1, image.size[0] - 1):
		for j in range(1, image.size[1] - 1):
			"""find RGB of image"""
			rgb = [
				[image.getpixel( (i - 1, j - 1) ), image.getpixel( (i, j - 1) ), image.getpixel( (i + 1, j - 1) )],
				[image.getpixel( (i - 1, j) ), image.getpixel( (i, j) ), image.getpixel( (i + 1, j) )],
				[image.getpixel( (i - 1, j + 1) ), image.getpixel( (i, j + 1) ), image.getpixel( (i + 1, j + 1) )]
			]
			tempx = [0, 0, 0];
			tempy = [0, 0, 0];
			
			"""Calculate x and y"""
			for k in range(0, 3):
				for l in range(0, 3):
					for m in range(0, 3):
						tempx[k] = tempx[k] + Gx[l][m] * rgb[m][l][k]
						tempy[k] = tempy[k] + Gy[l][m] * rgb[m][l][k]

			"""output RGB = (x^2 + y^2)^(1/2)"""
			temp = [0, 0, 0]
			for k in range(0, 3):
				temp[k] = int( math.sqrt( (tempx[k]**2 + tempy[k]**2) ) )

			outputimage.putpixel( (i, j), (temp[0], temp[1], temp[2]) )

	"""output image"""
	outputimage.save("edgedetection_" + imagefile)