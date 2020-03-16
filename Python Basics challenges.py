from random import *
"""
score = int(input("What was the student's score?"))

if score <= 90:
    if score < 60:
        print("This student receives an F.")
    if 60 < score < 70:
        print("This student receives a D.")
    if 70 < score < 80:
        print("This student receives a C.")
    if 80 < score < 90:
        print("This student receives a B.")
else:
    print("This student receives an A. Good job!")
"""
"""
rint = randint(1,10)

if rint == 1:
    print("The Roman numeral equivalent of " + str(rint) + " is I.")
elif rint == 2:
    print("The Roman numeral equivalent of " + str(rint) + " is II.")
elif rint == 3:
    print("The Roman numeral equivalent of " + str(rint) + " is III.")
elif rint == 4:
    print("The Roman numeral equivalent of " + str(rint) + " is IV.")
elif rint == 5:
    print("The Roman numeral equivalent of " + str(rint) + " is V.")
elif rint == 6:
    print("The Roman numeral equivalent of " + str(rint) + " is VI.")
elif rint == 7:
    print("The Roman numeral equivalent of " + str(rint) + " is VII.")
elif rint == 8:
    print("The Roman numeral equivalent of " + str(rint) + " is VIII.")
elif rint == 9:
    print("The Roman numeral equivalent of " + str(rint) + " is IX.")
else:
    print("The Roman numeral equivalent of " + str(rint) + " is X.")
"""
"""
usernum = int(input("Please type in a number."))
sum = 0
if usernum > 0:
    variable = usernum
    sum = variable
    while variable > 0:
        sum += variable - 1
        variable -= 1
    print("Your sum is " + str(sum) + " from the number you typed in, " + str(usernum))
"""
"""
userstr = str(input("Type in a word to see how many letters it is."))
letters = 0
if userstr != "":
    for letter in userstr:
        letters += 1
    print(str(letters))
    print(userstr)
"""
"""
for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
"""
"""
fact = int(input("Please enter a number to return a factorial."))
output = 1
for i in range(1,fact+1):
    output = output * i

print("The factorial of your number, " + str(fact) + " is: " + str(output))
"""
"""
mixed_case = "A Song of Ice and Fire"
title_case = mixed_case.title()
words = mixed_case.split()
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
print(words)
print("".join(words).isalpha())
"""
"""
the_string = "North Dakota"
center_plus = the_string.center(16, "+")
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))
"""
"""
user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)
"""

str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace():
        spaces_and_letters += char

words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)