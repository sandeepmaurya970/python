x=int(input("Enter a Number"))
c=0
while (x!=0):
	r=x%10
	print(r+1)
	x=x//10
	c=c+1
print("Number of digit in the Number = ",c)

input()
	