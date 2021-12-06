#Loops, Range & Code blocks
#Calculate average student height
student_heights = input("Input a list of students heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print (student_heights)

# to do an accumulative effect, you need to initially set the total to 0 so that iterative values can be saved
total_height = 0
for height in student_heights:
    total_height += height
    # += replaces "= total_height +"
print (total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
    # for every time ther's a number in the list, 1 is being added to the total number of students
print (number_of_students)

average_height = round(total_height/number_of_students)
print (f"The average height of the students is {average_height}")

student_scores = input("Input a list of student scores: ").split()
highest_score = 0
for score in (student_scores):
    score = int(score)
    if highest_score < score:
        highest_score = score
    else:
        highest_score = highest_score
print (f"The highest score in the class is {highest_score}")

for loops and the range () function
for number in range (1,10,2):
    print(number)
runs the code from 1 to 9 in increments of 2
total = 0
for number in range (1,101):
    total += number
print (total)

even_total = 0
for number in range (1,101):
    if number % 2 == 0:
        print (number)
        even_total += number
    else:
        continue
print (even_total)

#FizBuzz Interview Questions
for number in range (1,101):
    if number % 3 == 0:
        if number % 5 == 0:
            print ("FizzBuzz")
        else:
            print ("FIZZ")
    elif number % 5 == 0:
            print ("Buzz")
    else:
        print (number)
