def sort_list(lst):
	#if type(x) == list():
		
	n = len(lst)
	i = 0
	second_i = 0
	while i < n - 1:
	#	print ('i = ', i)
	#	print ('second_i = ', second_i)
		second_i = n - i - 1
		while second_i > i:

			if lst[i] > lst[second_i]:
			lst[i], lst[second_i] = lst[second_i], lst[i]
			second_i -= 1
		i += 1
	return lst 

#print (sort_list([1, 3, 2, 7]))
