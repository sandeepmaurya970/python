x=int(input("Enter a Number : \t"))
n=x
z=0
while(x!=0):
	y=x%10
	z=z+(y*y*y)
	x=x//10
if(z==n):
	print("This is armstrong number:\t",z)
else:
	print("\nThis is not armstrong Number:\t",n)




input()