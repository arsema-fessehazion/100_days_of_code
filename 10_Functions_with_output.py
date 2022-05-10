#def my_function():
#   result = 3 * 2
#    return result
# return is the end of the function, will not run anything following this as it has exited the function
def format_name():
    """This function withh ask the user to input their first and lat name and return a string with the capitalised starts"""
    f_name = input("Please enter your first name: ")
    l_name = input ("Please enter your last name: ")
    name = (f_name + " " + l_name).title()
    return name

print (format_name())

# Able to add multiple return statments through if statements

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
      return 29
  else:
     return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
