
dict = {} #creating dictionary

with open("document.txt", 'r') as file: #opening the text file and setting it equal to file
	
	lst = []
	for line in file:
		for word in line.split():
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 1

	sorted_dict = sorted(dict.items())
	lst = sorted(sorted_dict, key=lambda x:x[1], reverse=True)
	x = lst[1]
	#print(x[0],x[1])
	#print(lst[1])
	print('\r')
	for i in range(5):
		temp = lst[i]
		print(f'{temp[0]}: {temp[1]}')

