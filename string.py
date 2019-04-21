while True:
	string=input("Enter your string :")
	z=string.split(" ")
	print("Numbers of words in your string is: ",len(z))
	print("Your string in each seprate line with no. of latter")
	for word in z:
		print(word,"\t",len(word))
	
#	if
	while True:
		ch=input("Do you want to exit Y/N:")
		if ch=="y" or ch=="Y":
			print("Thanks for your valuable Time:")
			break
		else:
			print("Please Enter your valid Choice")
	break

		    