# expression
# HCF
# LCM
# POWER
# POWER ROOT
# FACTORIAL
# CONVERSION raidian to degre
# CONVERSION degree to radian
# trignametry function

import math
import datetime
def expr(a):
	return eval(a)
def hcf(q,w):
	t=math.gcd(q,w)
	return t
def lc(x1,x2):
	lcm=(x1*x2)/math.gcd(x1,x2)
	return lcm
def pw(x1,x2):
	return math.pow(x1,x2)
def pwr(x1,x2):
	return math.pow(x1,(1/x2))
def fact(n):
	return math.factorial(n)
def dr(x):
	return math.radians(x)
def rd(x):
	return math.degrees(x)
#def tri(x):
while True:
	aaj=datetime.datetime.today()
	print("\nToday date and Time is: ", end=" ")
	print(aaj)
	print("Press 1 for evaluating the expression")
	print("Press 2 for calculating the HCF ")
	print("Press 3 for calculating the LCM ")
	print("Press 4 for calculating the POWER ")
	print("Press 5 for calculating the root ")
	print("Press 6 for calculating the FACTORIAL ")
	print("Press 7 for calculating the conversion radian to degree")
	print("Press 8 for calculating the conversion degree to radian")
	print("Press 9 for calculating the Trignametry Function")
	print("Press 10 for exit:")
	ch=int(input())
	if ch==1:
		n=input("Enter the expression to evaluate: ")
		#print("Solution of this {} is {}")
		y=expr(n)
		print("Solution of the your expression {} is: = {}".format(n,float(y)))
		
	elif ch==2:
		n1=int(input("Enter first number: "))
		n2=int(input("Enter second number: "))
		y=hcf(n1,n2)
		print("\nThe HCF Your number {},{} is = {}".format(n1,n2,float(y)))
	elif ch==3:
		n1=int(input("Enter first number: "))
		n2=int(input("Enter second number: "))
		y=lc(n1,n2)
		print("\nThe LCM Your number {},{} is = {}".format(n1,n2,float(y)))
	elif ch==4:
		n1=int(input("Enter base number: "))
		n2=int(input("Enter POWER of the number: "))
		y=pw(n1,n2)
		print("\nPower of  Your number {},{} is = {}".format(n1,n2,float(y)))
	elif ch==5:
		n1=int(input("Enter the number: "))
		n2=int(input("Enter nth number: "))
		y=pwr(n1,n2)
		print("\nThe  {}th root of Your number {} is = {}".format(n2,n1,float(y)))
	elif ch==6:
		n=int(input("\nEnter  number: "))
		print("Factorial of the {} is ={}".format(n,fact(n)))
	elif ch==7:
		n1=int(input("\nEnter the angle in radian:"))
		print(" {} Radian is in Degree = {}".format(n1,float(rd(n1))))
	elif ch==8:
		n1=int(input("Enter the angle in degree:"))
		print(" {} Degree is in Radian= {}".format(n1,float(dr(n1))))
	elif ch==9:
		pass
	elif ch==10:
		print("********THANK YOU FOR YOUR VALUABLE TIME*********")
		break
	else:
		print("INVALID CHOICE")


input()		