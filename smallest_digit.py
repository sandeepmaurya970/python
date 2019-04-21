def smallest(n):
	min=n%10
	while(n!=0):
		r=n%10
		if(r<min):
			min=r
		n=n//10
	return min
while(True):

    x=int(input("\nEnter the Number:"))
    y=smallest(x)
    print("smallest digit among the number is:\t",y)
    ch=input("Do you Want to continue:Y/N   ")
    print("Enter your choice")
    if ch=='y' or ch=='Y':
    	True
    if ch=='n' or ch=='N':
    	break
    else:
    	print("Enter your Right choice")
print("thank you for your valuable Time")



input()