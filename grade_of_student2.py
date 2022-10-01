## Write a python program to calculate the grade of students in an exams.

#Your program should have (first name, last name, gender, student score)

    
#Your program should take keyboard input.


#follow these score;

#80 - 100 = pass

#60 - 79 = average

#39 - 59 = below average

#0 - 30 = fail

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

student_score = float(input("Enter your exam score: "))

# 80 - 100 = Pass
if student_score >= 80 and student_score <= 100:

	print(first_name, last_name, ", You have Passed")

elif student_score >= 60 and student_score <= 79:

	print(first_name, last_name, ", You are an average student")

elif student_score >= 39 and student_score <= 59:

	print(first_name, last_name, ", You are below average student")

else:

	print(first_name, last_name, ", You have FAILED")

