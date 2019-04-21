string=input("Enter your string :")
y=string.count(" ")   #count the string word seperated by space
print("Numbers of words in your string is: ",y+1)
z=string.split(" ") #split the string
print("Your string in each seprate line with no. of latter")
for word in z:
	print(word,"\t",len(word))


input()