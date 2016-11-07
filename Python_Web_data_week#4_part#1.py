import urllib
from BeautifulSoup import *
import re
url = raw_input('Enter -')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
total = 0
for tag in tags:
	total = total + int(tag.contents[0])
print total