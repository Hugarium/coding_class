#ask a user to enter their age, sex, marital status and then use the following rules print their place of service

### Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

##if emplo s female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

### And any other input of age should print "ERROR"

##taking age of user
age = int(input("enter your age: "))

#asking user to enter their sex
sex = input("enter your sex: M/F: ")

#asking a user to enter their marital status

marital_status = input("Are you married?: Y/N: ")

#if employee is female, then she will work only in urban areas
if sex == "F":
	print(sex, ",Post to urban areas only")

elif sex == "M" and age >= 20 and age <= 40:

	print("may work anywhere")

elif sex == "M" and age >= 40 and age <= 60:


	print("work in urban areas only")

else:

	print ("ERROR")



















