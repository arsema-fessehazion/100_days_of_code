# Dictionaries & Nesting

# Dictionaries: KEY AN VALUE
#{KEY:VALUE}

#be careful for the way inwhich you show the dictionary, have each pair on own like and curly bracets by themselvfes. Last bracket with no indent
#always end each line with a comma incase need to add more in future
programing_dictionary = {
    "Key":"This is the value",
    "another key":"another value to be printed",
}

#To retrieve an item from the dictionary, highlight the key you want and it will print out the VALUE
print(programing_dictionary["another key"])

#Adding a new entry
programing_dictionary["loop"] = "Adding a new entry ito the dictionary"
print(programing_dictionary)

#creat an empty dictionary in sam way done by lists, empty_list = []
empty_dictionary = {}

#can wipe an existing dictionary
programing_dictionary = {}
print(programing_dictionary)

#Can edit an item in empty_dictionary
programing_dictionary["Key"] = "It has now changed"
print(programing_dictionary)

#Loop throuh a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])
    #using retrieval code to get the value

Grading program

student_scores = {}

student_name = input("Please enter the student's name: ")
student_grade = int(input("What is their score: "))

if student_grade >= 91:
    print("Outstanding")
elif student_grade >= 81 and student_grade <= 90:
    print("Exceeds expectations")
elif student_grade >= 71 and student_grade <= 80:
    print("Acceptable")
else:
    print("Fail")

student_scores = {
    "Harry":81,
    "Ron" : 78,
    "Hermoine" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

#emtpy code
student_grades = {}

#write code to add grades to the dictionary
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] ="Exceeds expectations"
    elif score >= 70:
        student_grades[student] ="Acceptable"
    else:
        student_grades[student] ="Fail"
print(student_grades)

#Nesting
# storing folders within eachother
# {
# key: Value
# key:[List]
# key:{Dict}
# }

# list in a dictionary
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany":["Berlin", "Munich", "Frankfurt"],
}

# dictionary in a dictionary
travel_log = {
    "France": {"cities_visted": ["Paris","Lille","Dijon"],"total_visits": 12},
    "Germany":{"cities_visted": ["Berlin", "Munich", "Frankfurt"],"total_visits": 5}
}

#nesting dictionary in a list
travel_log = [
    {
        "country" : "France"
        "cities_visted": ["Paris","Lille","Dijon"],
        "total_visits": 12
    },
    {
        "Country" : "Germany"
        "cities_visted": ["Berlin", "Munich", "Frankfurt"],
        "total_visits": 5
    },
]

Coding exercise, dictionary in List
travel_log = [
    {
        "country" : "France",
        "cities_visted": ["Paris","Lille","Dijon"],
        "total_visits": 12,
    },
    {
        "Country" : "Germany",
        "cities_visted": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

#need to append the trael log lists
new_country = input("Enter new country travelled to: ")
new_cities = input("What cities did you travel to, seperated by a comma:  ").split(",")
number_of_visits = int(input("How many times have you visited here: "))

new_country_dictionary = {
    "Country" : new_country,
    "cities_visted": new_cities,
    "total_visits": number_of_visits,
}

travel_log.append(new_country_dictionary)
print(travel_log)


#to creat in funtion form:

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country ["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print (travel_log)
