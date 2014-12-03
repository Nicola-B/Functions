#Nicola Batty
#03/12/2014
#Functions Revision Exercises 3

def pramiter_order():
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter anuther number: "))
    if number1 < number2:
        print("{0}, {1}".format(number1, number2))
    else:
        print("{0}, {1}".format(number2, number1))
