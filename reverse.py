def reverse(n):
	rev=0
	while(n!=0):
		r=n%10
		rev=rev*10+r
		n=n//10
	return rev
x=int(input("\nenter a number:\t"))
y=reverse(x)
print("\nReverse of the number is \t",y)


input()