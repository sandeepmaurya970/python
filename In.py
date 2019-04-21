while True:
	name=input("Enter your full name.(FirstName MiddleName LastName) ")

	listOfWord=name.split(" ")
	# print(listOfWord)

	if len(listOfWord)==3:
		print(name.title())
		print(listOfWord[0][0].upper()+". ",end='')
		print(listOfWord[1][0].upper()+". ",end='')
		print(listOfWord[2])

		print(listOfWord[2].title()+" ",end='')
		print(listOfWord[0][0].upper()+". ",end='')
		print(listOfWord[1][0].upper()+". ")
	else:
		print("invalid name..")
	i=input("Do you want to exit Y/N")
	if i=='Y':
		break





	