
dict = {} #creating dictionary

with open("document.txt", 'r') as file: #opening the text file and setting it equal to file
	lst = []
	for line in file:
		for word in line.split():
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 1
	#dict_lst = dict.items()
	sorted_dict = sorted(dict.items())
	lst = sorted(sorted_dict, key=lambda x:x[1], reverse=True)[:5]

	for i in lst:
		print(f'{i} :{dict[i]}')



