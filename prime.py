x=int(input("Enter the Number"))
c=0
for i in range(1,x+1):
	if(x%i==0):
		c=c+1
if(c==2):
	print("Number is prime")
else:
	print("Number is not prime")


input()