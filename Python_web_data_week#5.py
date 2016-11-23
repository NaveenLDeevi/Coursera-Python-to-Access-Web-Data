import urllib
import xml.etree.ElementTree as ET
url = raw_input("Enter URL:")
uh = urllib.urlopen(url)
data = uh.read()
print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')

lst = tree.findall('comments/comment')
num_list = []
for i in lst:
	number = i.find('count').text
	num_list.append(int(number))

print sum(num_list)
	


