#Nicola Batty
#02/12/2014
#Function Revistion exercises 2

def input_number():
    number1 = even
    while number1 == "even":
        number = int(input("please enter a odd number: "))
        if not number/2:
            number1 = "odd"
        else:
            number1 = "even"
    return number

def display_star_pyramid(number):
    while number > 1:
        print("*" * number)
        number = number - 2

def star_pyramid():
    number = input_number()
    display_star_pyramid(number)
