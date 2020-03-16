from random import *

#number = int(input("Please type in a number to be added to 10."))
#print(number + 10)


print(randint(10, 20))
def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")


prints_four()
prints_four()
prints_four()
prints_four()
prints_four()

#def function_name(parameter):
#    print(parameter+2)


#function_name(8)
first_str = "The number "

def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name(first_str, 5, " is an integer.")

def default_example(num1=7, num2=8):
    return num1 * num2



print(default_example() + 44)

#Celsius to Fahrenheit challenge
celsius = int(input("Please put in a C temperature to convert to F."))

def temp_conversion(celsius):
    return round((1.8 * celsius + 32), 2)


print("The Fahrenheit equivalent to " + str(celsius) + " degrees Celsius is " + str(temp_conversion(celsius)) + ".")


print(randint(1,10))


#MPG challenge

fueltank = randint(10,25)
milespertank = randint(200,400)

milespergallon = milespertank // fueltank

print(milespergallon)
print(milespertank, milespergallon)


print("hello" == "hello")

veg = input("Type the name of a vegetable.")

if veg == "corn":
    print("The vegetable is corn.")
else:
    print("The vegetable is not corn.")

gpa = float(input("What was the applicant's grade point average?"))
inst_app = input("Is the student going to be educated at an approved institution?")

if gpa >= 3.7:
    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan.")
    else:
        print("The applicant did not have high enough grades to qualify.")
else:
    print("The applicant did not have high enough grades to qualify.")

#format function notes!!

name = input("What is the job applicant's name?")
degree = input("What did they major in at college?")
job = input("What is their current occupation?")
experience = input("How many years have they been working in their field?")

print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))