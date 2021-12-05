#My attempt at a Tip Calculator
print("Welcome to the tip calculator.")
total_amount = float(input("What was the total bill? £"))
no_of_guests = int(input("How many people to split the bill? "))
bill_tip = int(input("What % tip would you like to give? 10, 12 or 15? "))

tip_increase = bill_tip /100
total_plus_bill = total_amount + (total_amount * tip_increase)
split_bill = float(total_plus_bill/no_of_guests)

print(f"Each person should pay: £{split_bill:.2f}")

# program that adds the digits
two_digit = (input("Please state a 2-digit number: "))
a = int(two_digit[0])
b = int(two_digit[1])
c = a+b
print(f"The sum of your double digit is {c}")

#BMI Calculator Challenge
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = int(weight/(height**2))
print(f"Based on your height & weight, your BMI is {bmi} kg/m^2")

#Your life in weeks
total_life_in_years = 90
total_life_in_months = total_life_in_years * 12
total_life_in_weeks = total_life_in_years * 52
total_life_in_days = total_life_in_years * 365

user_age = int(input("Please state your age: "))
user_age_in_months = user_age * 12
user_age_in_weeks = user_age * 52
user_age_in_days = user_age * 365

remaining_months = total_life_in_months - user_age_in_months
remaining_weeks = total_life_in_weeks - user_age_in_weeks
remaining_days = total_life_in_days - user_age_in_days

print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left")
