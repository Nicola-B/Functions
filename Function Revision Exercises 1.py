#Nicola Batty
#02/12/2014
#Function Revision Exercises 1

def input_number_and_symbol():
    symbol = input("please enter a caricter: ")
    number = int(input("please enter the number of times you whant this caricter to be printed: "))
    return symbol, number

def display_symbol(symbol,number):
    print(symbol * number)

def output_symbol():
    symbol, number = input_number_and_symbol()
    display_symbol(symbol,number)
