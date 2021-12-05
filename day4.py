import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

# heads or tails exercise
import random
coin_flip = random.randint(1,2)

if coin_flip == 1:
    print("Heads")
else:
    print("Tails")

#Coding Challenge
#Who's paying the bill
import random

names_string = input("Give me everybody's name, seperated by a comma: ")
names = names_string.split(",")
total_players = int(len(names)) - 1

random_name = random.randint(0,total_players)

print(f"{names[random_name]} is the lucky winner paying for the bill :)")
#---------------------------------------------------------------------------------------
names_string = input("Give me everybody's name, seperated by a comma: ")
names = names_string.split(",")
print(f"{random.choice(names)} is the lucky winner paying for the bill :)")
