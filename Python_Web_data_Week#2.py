import re
addin = list()
sum = 0
name = raw_input('Enter the name of the file:')
fhandle = open(name)
for lines in fhandle:
	y = re.findall('[0-9]+',lines)
	addin.extend(y)
for i in addin:
	i = int(i)
	sum = sum + i
print sum