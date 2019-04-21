x=int(input("Enter the number of rows: "))
for row in range(1,x+1):
	for col in range(1,row+1):
		if col>=row-1 and col<=row+1:
			print("*",end=" ")
		else:
			print(end=" ")
	print()



