def even(n):
	if(n%2==0):
		return True
	else:
		return False
x=int(input("\nEnter a number:\t"))
sum=0

while(x!=0):
	y=x%10
	x=x//10
	if(even(y)):
		sum=sum+y
	else:
		pass
print("sum=\t",sum)



input()