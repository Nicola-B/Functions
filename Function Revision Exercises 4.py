#Nicola Batty
#04/12/2014
#Function Revision Exorcises 4

def input_fahrenheirt():
    fahrenheirt = int(input("Please enter the fahrenheirt you whant to convert: "))
    return fahrenheirt

def calculate_celsius(fahrenheirt):
    celsius = (fahrenheirt - 32) * (5/9)
    return celsius

def display_celsius(celsius,fahrenheirt):
    print("{0:.2f}fahrenheirt = {1:.2f}celsius".format(fahrenheirt, celsius))

def convert_temps():
    fahrenheirt = input_fahrenheirt()
    celsius = calculate_celsius(fahrenheirt)
    display_celsius(celsius,fahrenheirt)
