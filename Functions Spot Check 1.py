#Nicola Batty
#09/12/2014
#Functions Spot Check 1

def password_too_short():
    print("Password too short, try again.")
    password1 = "wrong"
    return password1

def password_too_long():
    print("Password too long, try again.")
    password1 = "wrong"
    return password1

def password_right():
    print("Parssword accepted.")
    password1 = "Right"
    return password1

def password_right_or_wrong(password):
    if password > 16:
        password1 = password_too_long()
    elif password < 8:
        password1 = password_too_short()
    else:
        password1 = password_right()
    return password1

def create_password():
    password1 = "wrong"
    while password1 == "wrong":
        password = input("Please input paerssword 8-16 charcters long: ")
        password1 = password_right_or_wrong(password)
