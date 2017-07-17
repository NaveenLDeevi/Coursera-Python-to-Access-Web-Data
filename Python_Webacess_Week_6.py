import urllib
import json

address = raw_input("Enter the URL:")
print "Retreiving"
uh = urllib.urlopen(address)
data = uh.read()
js = json.loads(str(data))
sum_list = []
for i in js["comments"]:
	sum_list.append(i["count"])
print sum(sum_list)
