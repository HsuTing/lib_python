# -*- coding:utf-8 -*-
import Image

def histogramequalization(imagefile):
	image = Image.open(imagefile)
	outputimage = Image.new( "RGB", (image.size[0], image.size[1]) )

	"""use for recording R, G, B"""
	R = {}
	G = {}
	B = {}
	"""use for recording min of R, G, B"""
	channel={
		"R": 0,
		"G": 0,
		"B": 0,
	}

	"""set RGB to zero"""
	for i in xrange(256):
		R[i] = 0
		G[i] = 0
		B[i] = 0

	"""count GRB"""
	for i in xrange(image.size[0]):
		for j in xrange(image.size[1]):
			rgb = image.getpixel( (i, j) )
			R[rgb[0]] += 1
			G[rgb[1]] += 1
			B[rgb[2]] += 1

	"""count cdf"""
	for i in range(1, 256):
		R[i] = R[i] + R[i - 1]
		G[i] = G[i] + G[i - 1]
		B[i] = B[i] + B[i - 1]

	"""find min in GRB"""
	channel["R"] = findmin(R)
	channel["G"] = findmin(G)
	channel["B"] = findmin(B)

	"""histogram equalization"""
	for i in xrange(image.size[0]):
		for j in xrange(image.size[1]):
			rgb = image.getpixel( (i, j) )
			tempr = normalize(image, R[rgb[0]], channel["R"])
			tempg = normalize(image, G[rgb[1]], channel["G"])
			tempb = normalize(image, B[rgb[2]], channel["B"])
			outputimage.putpixel( (i, j), (tempr, tempg, tempb) )

	"""output image"""
	outputimage.save("histogramequalization_" + imagefile)

"""find min"""
def findmin(channel):
	for i in xrange(256):
		if channel[i] != 0:
			return channel[i]

"""count every channel"""
def normalize(image, channel, channelmin):
	temp = (channel - channelmin) * (256 - 1) / ( (image.size[0] * image.size[1]) - channelmin)
	return temp