# number=int(input("Enter number"))
# if(number<0):
# 	print("negative")
# elif(number>0):
# 	print("Positive ")
# else:
# 	print("Number is zero")

# n=int(input("Enter new number"))
# if(n%2==0):
# 	print("Number is even")
# else:
# 	print("Odd number")
m=int(input("enter lower bound"))
n=int(input("enter upper bound"))
sum=0
for i in range(m,n+1):
	sum=sum+i

print("Sum is ",sum)



input()