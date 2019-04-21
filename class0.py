import time
import datetime

#import os
class A:
	def __init__(self):
		self.a=35
		self.b=12
		print(self.a*self.b)

class B(A):
	def clear():
		import os
		os.system('cls')
o=A()
print(o.a)
print(o.b)
time.sleep(2.0)    #to give the delya of 2 seconds.
#os.system('cls')
print(o.a)
print(o.b)
ob=B()
B.clear()
print(o.b)
print(o.a)
print(o.b)
print(o.a)
print(o.b)
now=datetime.datetime.now()
print(now)
#print(datetime.date())




