def sorting_list(numbers):
	for i in range(0,len(numbers)):
		for j in range(0,len(numbers)):
			if i > j:
				numbers[i],numbers[j] = numbers[j],numbers[i]
	return numbers

print(sorting_list([7,4,2,1]))