#Nicola Batty
#18/11/2014
#Calulating pay starter

#defining a function
def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calaculate_overtime_pay(hours,pay):
    overtime_pay = (hours - 40) * (pay * 1.5)
    basic_pay = pay * 40
    total = overtime_pay + basic_pay
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calaculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("please input the number of hours worked: "))
    pay = float(input("please input the rate of pay: "))
    return hours, pay

def display_mouny_erned(total):
    print("They have earned £{0}".format(total))

def calculat_pay():
    hours, pay = work_details()
    total = calculate_total_pay(hours,pay)
    display_mouny_erned(total)
