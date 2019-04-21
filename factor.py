x=int(input("Enter a number="))
sum=0  #for sum of the factor
c=0  #for count of the factor
for i  in range(1,x+1):
	if(x%i==0):
		print(i)
		sum=sum+i   #for sum of the factor
		c=c+1    #for count of the factor
print("number of factor are=",c)
print("sum of factor=",sum)




input()
