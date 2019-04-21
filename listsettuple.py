
x=int(input("Enter the no.of student: "))
students={}
for i in range(1,x+1):
	print("Enter the student name",i,':',end=' ')
	input()
	sub=input("Enter the Subject Name: ")
	marks=int(input("Enter the Marks of Subject: "))
	student={"{}",sub :"{}",marks}
	students.append(stname)
setstname=set(students)
print("\n The students Name are: ",setstname)