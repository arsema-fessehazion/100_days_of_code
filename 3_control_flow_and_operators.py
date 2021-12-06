#Odd or Even
user_input = int(input("Please state a number: "))
if user_input % 2 == 0:
    input_half = user_input/2
    print(f"Your number {user_input} is even")
else:
    print (f"Your number {user_input} is odd")

#Nested if statements
# BMI calculater 2.0
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = int(weight/(height**2))
print(f"Based on your height & weight, your BMI is {bmi} kg/m^2")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi <30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")

# If any given year is a leap Year
year = int(input("Which year did you want to check? "))

if year % 100 == 0:
    if year % 4 == 0 and year % 400 == 0:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")
else:
    print(f"The year {year} is not a leap year")

 #Pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_size = 15
medium_size = 20
large_size = 25
pepperoni_small = 2
pepperoni_med_large = 3
extra_cheese_price = 1

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total_price = small_size + pepperoni_small +extra_cheese_price
        else:
            total_price = small_size + pepperoni_small
    else:
        total_price = small_size
else:
    total_price = small_size

if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total_price = medium_size + pepperoni_med_large + extra_cheese_price
        else:
            total_price = medium_size + pepperoni_med_large
    else:
        total_price = medium_size
else:
    total_price = medium_size

if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total_price = large_size + pepperoni_med_large +extra_cheese_price
        else:
            total_price = large_size + pepperoni_med_large
    else:
        total_price = large_size
else:
    total_price = large_size

print(f"Your final bill is £{total_price}")

# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_caps = name1.upper()
name2_caps = name2.upper()

letter_t = name1_caps.count("T") + name2_caps.count("T")
letter_r = name1_caps.count("R") + name2_caps.count("R")
letter_u = name1_caps.count("U") + name2_caps.count("U")
letter_e = name1_caps.count("E") + name2_caps.count("E")
letter_l = name1_caps.count("L") + name2_caps.count("L")
letter_o = name1_caps.count("O") + name2_caps.count("O")
letter_v = name1_caps.count("V") + name2_caps.count("V")

number1 = str(letter_t+letter_r+letter_u+letter_e)
number2 = str(letter_l+letter_o+letter_v+letter_e)
score = int(number1+number2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")




