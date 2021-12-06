#Breaking a complexproblem down into a flow chart
#Function Parameters with inputs

def greet():
    name = input("What is your Name? ")
    print (f"hi {name}")
    print ("hi")
    print ("hi")

greet()

#                   PARAMETER - used inside the function
def greet_with_name(their_name):
    print (f"hi {their_name}")
    print ("hi")
    print ("hi")
# check that the variable is in strng form if using the f function to print it out

#                ARGUMENT
greet_with_name("Arsema")

#POSTIONAL VS KEYWORD ARGUMENTS
#function wit more han 1 input

def greet_with(name,location):
    print (f"Hi, {name}! \nHow are thing's in {location}?")

greet_with("Arsema","London")

#changing the order with keyword arguments
def greet_with(name,location):
    print (f"Hi, {name}! \nHow are thing's in {location}?")

greet_with(name = "Arsema",location = "London")
greet_with(location = "London", name = "Arsema")

#Calculate number of paint cans
def get_input():
    test_h = int(input("Height of the wall, m^2: "))
    test_w = int(input("Width of wall, m^2: "))
    coverage = int(input("1 paint covers how much wall, m^2: "))
    user_inputs = [test_h,test_w,coverage]
    return (user_inputs)

def paint_calc(wall_height, wall_width, paint_coverage):
    number_of_cans = round((wall_height * wall_width)/ paint_coverage)
    print (f"You will need {number_of_cans} paint cans to cover your wall!")


user_inputs = get_input()
paint_calc(wall_height = user_inputs[0], wall_width = user_inputs[1], paint_coverage = user_inputs[2])


#Prime Number Check - basic
def prime_checker(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        print (f"{number} is a print number")
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number = n)
