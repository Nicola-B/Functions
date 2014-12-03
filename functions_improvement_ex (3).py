#Nicola Batty
#21/11/2014
#functions improvement exercise
#times-table tester

import random

def ans(num1,num2):
    ans = num1 * num2
    return ans

def user_ans(num1,num2):
    user_ans = int(input(str(num1) + " x " + str(num2) + " = "))
    return user_ans

def input_num1():
    num1 = int(input("Which times-table do you want to be tested on? "))
    return num1

def right_or_wrong(num1,num2):
    ans = ans(num1,num2)
    user_ans = user_ans(num1,num2)
    if user_ans == ans:
        user_ans = "ture"
        return user_ans,ans
    else:
        user_ans = "fuls"
        return user_ans,ans
def display_right_or_wrong(user_ans,ans):
    if user_ans == "ture":
        print("Well done, you got the correct answer!")
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)

def times_table():
    num1 = input_num1()
    num2 = random.randrange(2,13)
    for quesions in range(1,6):
        user_ans,ans = right_or_wrong(num1,num2)
        display_right_or_wrong(user_ans,ans)

# main program
#print("Times-table tester")
#print()
#testTable = input("Which times-table do you want to be tested on? ")
#testTable = int(testTable)
#for questions in range(1,6):
#    Num1 = testTable
#    Num2 = random.randrange(2,13)
#    Ans = Num1 * Num2
#    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
#    UserAnswer = int(UserAnswer)
#    if UserAnswer == Ans:
#        print('Well done, you got the correct answer!')
#        print()
#    else:
#        print('Sorry, you got the answer wrong. The correct answer is',Ans)
#        print()
              
