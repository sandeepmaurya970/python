import math
n=int(input("Enter the number"))

c=0

n1=n

while(n!=0):
	r=n%10
	c=c+1
	n=n//10

# print("Number ",c ," its ok..")
print("Number of digits = ",c)

d=math.pow(10,c-1)


while(n1!=0):
	f=n1//d
	print(int(f+1))
	n1=n1%d
	d=d//10


input()