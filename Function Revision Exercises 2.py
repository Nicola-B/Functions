#Nicola Batty
#02/12/2014
#Function Revistion exercises 2

def input_number():
    number1 = "even"
    while number1 == "even":
        number = int(input("please enter a odd number: "))
        if number%2 == 0:
            number1 = "even"
        else:
            number1 = "odd"
    return number

def display_star_pyramid(number):
    while number > 0:
        print("*" * number)
        number = number - 2

def star_pyramid():
    number = input_number()
    display_star_pyramid(number)
