while True:
	a=0
	b=1
	feb=0
	for i in range(51):
		feb=a+b
		print("{}.   {}".format(i,feb))
		b=a
		a=feb
	ch=input("do you want to exit:")
	if ch=='y' or ch=='Y':
		break