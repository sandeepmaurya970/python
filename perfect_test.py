from math import *
number=float(input("Enter the Number: "))
a=floor(number)
a=str(a)
c=number-int(a)
real=(a[-1:-len(a)-1:-1])
print(real,end=" ")
c=str(c)
print(c[-1:-len(c)-1:-1])