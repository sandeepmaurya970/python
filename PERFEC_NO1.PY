x=int(input("Enter a number="))
for i in range(1,x+1):
	sum=0
	for r in range(1,i):
		    if(i%r==0):
			    sum+1
	if (sum==i):
		print(i)
