def print_pyramid_pattern(number_of_rows):
	for i in range(1,number_of_rows+1):
		for k in range(number_of_rows,i,-1):
			print(' ',end='')
		for j in range(0, 2 * i - 1):
			print('*',end='')
		print()


print_pyramid_pattern(7)