
def isPrime(n):
	c=0
	for i in range(1,n+1):
		if(n%i==0):
			c=c+1

	if(c==2):
		return True
	else:
		return False

#=========================================
# ans=isPrime(6)
# if(ans==True):
# 	print("number is prime")
# else:
# 	print("number is not prime..")

# ans1=isPrime(565)
# print(ans1)

n=int(input("Enter the number"))
for i in range(1,n+1):
	if(n%i==0):
		if(isPrime(i)):
			print(i)


input()