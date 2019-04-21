x=int(input("Enter a number="))
n=x
sum=0  #for sum of the factor
# c=0  #for count of the factor
for i  in range(1,x):
	r=i
	if(x%i==0):
		print(i)
		sum=sum+i   #for sum of the factor
		# c=c+1
	if(sum==r):
	print("This is perfact number")
	print(r)
else:
	print("Not a perfact number")
		   #for count of the factor
#print("number of factor are=",c)
#print("sum of factor=",sum)
# if(sum==r):
# 	print("This is perfact number")
# else:
# 	print("Not a perfact number")



input()