import urllib2

"""get data from web"""
def fromweb(url, name):
	for i in range(0, len(url)):
		content = urllib2.urlopen(url[i])
		data = content.read()
		fout = open(name[i], 'w+')
		fout.write(data)
