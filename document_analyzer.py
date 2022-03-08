
#file1 = open(document.txt) #allows text to be read
#info = file1.read() #reads individual words

filename = "document.txt"

for line in open(filename, 'r'):
	#print(len(line))
	for i in line:
		print(i)

