#Write a python program for the user.
#A school has following rules for grading system.

#a. Below 25 - F

#b. 25 to 45 - E

#c. 45 to 50 - D

#d. 50 to 60 - C

#e. 60 to 80 - B

#f. Above 80 - A

#Ask user to enter marks and print the corresponding grade


#taking students exam marks
marks_obtained = float(input("input mark obtained: "))


#a. Below 25 - F
if marks_obtained >0 and marks_obtained < 25:

	print("F")

#b. 25 to 45 - E
elif marks_obtained >=25 and marks_obtained <=45:

	print("E")
	
#c. 45 to 50 - D
elif marks_obtained >= 45 and marks_obtained <= 50:

	print("D")

elif marks_obtained>= 50 and marks_obtained <= 60:

	print("C")

elif marks_obtained >= 60 and marks_obtained <= 80:

	print("B")


elif marks_obtained > 80 and marks_obtained <= 100:

	print("A")

else:

	print("Marks obtained is out of range")





