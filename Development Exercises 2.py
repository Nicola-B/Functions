#Nicola Batty
#05/12/2014
#Development Exercises 2

def input_number():
    number1 = "even"
    while number1 == "even":
        number = int(input("please enter a odd number: "))
        if number%2 == 0:
            number1 = "even"
        else:
            number1 = "odd"
    return number

def display_top_pyramid(number):
    number1 = 1
    for number1 in range(1,number,2):
        print("*" * number1)
        number1 = number1 + 2

def display_bottom_pyramid(number):
    while number > 0:
        print("{0:^}".format("*") * number)
        number = number - 2

def star_Dimond():
    number = input_number()
    display_top_pyramid(number)
    display_bottom_pyramid(number)

