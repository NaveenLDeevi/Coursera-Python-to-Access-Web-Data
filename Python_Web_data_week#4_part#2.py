import urllib
from BeautifulSoup import *
import re
x1 = raw_input('Enter -')
count = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))
def url_open(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	return tags
counter1 = 0
Pos_counter = 0
while(counter1< count):
	counter1 = counter1 + 1
	tags = url_open(x1)
	
	for tag in tags:
		Pos_counter = Pos_counter + 1
		if Pos_counter < position:
			continue
		elif Pos_counter == position:
			x1 = tag.get('href',None)
			print x1
			Pos_counter = 0
			break
		break