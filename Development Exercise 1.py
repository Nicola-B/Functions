#Nicola Batty
#05/12/2014
#Development Exercise 1

def calculate_number_of_hours(hours):
    minutes = hours*60
    seconds = minutes*60
    return seconds

def calculate_number_of_minutes(minutes):
    seconds = minutes*60
    return seconds

def input_hours_minutes_and_seconds():
    hours = int(input("Pleses enter the number of hours: "))
    minutes = int(input("Pleses enter the number of minutes: "))
    seconds = int(input("Pleses enter the number of seconds: "))
    return hours,minutes,seconds

def calculate_number_of_seconds(hours,minutes,seconds):
    seconds1 = calculate_number_of_hours(hours)
    seconds2 = calculate_number_of_minutes(minutes)
    seconds =  seconds + seconds1 + seconds2
    return seconds

def display_seconds(seconds):
    print(seconds)

def number_of_seconds():
    hours,minutes,seconds = input_hours_minutes_and_seconds()
    seconds = calculate_number_of_seconds(hours,minutes,seconds)
    display_seconds(seconds)
