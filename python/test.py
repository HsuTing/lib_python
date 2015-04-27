import sys
sys.path.append("/home/hsuting/library/python/data")
import get_data
from get_data import From_web

url = [
	'http://opendata.epa.gov.tw/ws/Data/SGWC/?$format=xml',
]

name = [
	'SGWC'
]

From_web(url, name)
