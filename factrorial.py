def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
while True:
    x=int(input("Enter a Number :"))
    y=fact(x)
    print("factrial of" ,x,"is",y)
    ch=input("Do you want to Exit Y/N:")
    if ch=='y':
    	print("Thanks for your valuable Time:")
    	break
