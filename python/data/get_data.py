import urllib2

def Get_jaon_from_web(utl, output):
	content = urllib2.urlopen(url)
	data = content.read()
	fout = open(output, 'w+')
	fout.write(data)
