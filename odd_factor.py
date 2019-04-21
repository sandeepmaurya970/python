x=int(input("Enter a number"))
c=0
sum=0
for i in range(1,x+1):
	if(x%i==0):
		if(i%2!=0):
			print(i)
			sum=sum+i
print("sum of all odd factor",sum)

input()