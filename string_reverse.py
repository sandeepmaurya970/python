print("press 1 for reverse of string")
print("press 2 for length of string")
print("press 3 for upper case of string")
print("press 4 for upper case of string")
ch=int(input())
n=input("Enter the your string string : ")
if ch==1:
	print("Your reverse string")
	print(n[-1:-len(n)-1:-1])
if ch==2:
	print("length of your string is : ",len(n))
if ch==3:
	print("Your string in upper case")
	print(n.upper())
if ch==4:
	print("Your string in lower case")
	print(n.lower())
