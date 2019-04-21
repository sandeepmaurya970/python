def prime(n):
	c=0
	for i in range(1,n+1):
		if(n%i==0):
			c=c+1	
        if c==2:
        	print True
        else:
    	    print False
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
y=int(input("enter a number"))
for i in range(1,y+1):
	if(y%i==0):
		if(prime(i)):
			print("the prime factor are",i)



input()