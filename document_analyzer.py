
#file1 = open(document.txt) #allows text to be read
#info = file1.read() #reads individual words

#filename = "document.txt"

#for line in open(filename, 'r'):
	#print(len(line))
#	for i in line:
#		print(i)
dict = {}

with open("document.txt", 'r') as file:
	for line in file:
		for word in line.split():
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 1
	lst = sorted(dict, key=dict.get, reverse=True)[:5]
	for i in lst:
		print(f'{i}: {dict[i]}')
	#print(lst)



