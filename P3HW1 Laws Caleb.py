#Caleb Laws
#3/28/2026
#P3HW1 - Grade Calculator
# This program will show the grades of each module then calculate or show the lowest grade, highest grade, the sum of the grades, and the average grade, it will then assigne a letter grade to the average grade and show it to the user.

# Get 6 different grades from the user
module1_grade = float(input("Enter the first grade: "))
module2_grade = float(input("Enter the second grade: "))
module3_grade = float(input("Enter the third grade: "))
module4_grade = float(input("Enter the fourth grade: "))
module5_grade = float(input("Enter the fifth grade: "))
module6_grade = float(input("Enter the sixth grade: "))

#Analyze the grades and calculate the lowest grade, highest grade, sum of the grades, and average grade
grades = [module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade]
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

#Print the results to the user
print("Grades: ", grades)

print("----------Results----------")
print("Lowest Grade: ", lowest_grade)
print("Highest Grade: ", highest_grade)
print("Sum of Grades: ", sum_of_grades)
print("Average Grade: ", average_grade)

# With the given information, assign a letter grade to the average grade and show it to the user
if average_grade >= 90:
    letter_grade = "A" 
elif average_grade >= 80:
    letter_grade = "B"
elif average_grade >= 70:
    letter_grade = "C"
elif average_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print ("----------Letter Grade----------")
print("Letter Grade: ", letter_grade)

