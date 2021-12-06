print("Python print function")
print("The function is declared like this:")
print("print ('what to print')")

#Debugging exercise

print("Day 1 - String Manipulation")
print("String concatentation is done with the + " + "sign")
print('e.g print ("Hello ' + 'World")')
print("New lines can be created \n with a backslash n")

#Input function
name = input("Please state your name: ")
name_len = len(name)
print(f"Your name has {name_len} characters!")

#Python Variables
a = input("a:")
b = input("b:")

a_new = b
b_new = a

print(f"a = {a_new}")
print(f"b = {b_new}")

#Band name generator project
name = input("Hello! Welcome to Band Name Generator!\nWhat is your name? ")
city = input("What city did you grow up in? ")
band_name = name + " " + city

print(f"Your new band name is '{band_name}'")
