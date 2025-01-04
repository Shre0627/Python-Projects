# Shreya Jamnadas
# December 26 2024
# Creating a Password Validator Program using functions, if statements, loops, user input, and try and catch

# Password Validator
# Requirements:
# Password Length should be between 8-20 characters
# password should contain a lowercase letter, upercase letter, digit, and special character
# should not be a simple sequence and shouldn't include the username and no spaces

# function for each checker
def isDigitCheck(pw):
    check = False
    for x in pw:
      if x.isdigit():
          check = True
          break
    return check

def upperLetter(pw):
    check = False
    for x in pw:
        if x.isupper():
            check = True
            break
    return check

def lowerLetter(pw):
    check = False
    for x in pw:
        if x.islower():
            check = True
            break
    return check
            
def specialCharCheck(pw):
    check = False
    for x in pw:
        if x == "@" or x == "$" or x == "#" or x == "!" or x == "%":
            check = True
            break
    return check

username = input("Enter your username: ")
while True:
    password = input("Enter your password: ")
    password = password.strip()
    try:
        searchSpace = password.find(" ")
        assert searchSpace < 0, "Password contains whitespace"
        assert len(password) >= 8, "Password length is too short"
        assert len(password) <= 20, "Password length is too long"
        assert isDigitCheck(password), "Password doesn't contain a digit"
        assert lowerLetter(password), "Password doesn't contain a lower-case letter"
        assert upperLetter(password), "Password doesn't contain a upper-case letter"
        assert specialCharCheck(password), "Password doesn't contain a special character"
        #check if username is not part of pw
        searchUser = password.find(username) # search for the username in password
        assert searchUser < 0, "Password contains username"
        # search for simple sequences
        search = password.find("assword")
        assert search < 0, "Password shouldn't contain the word \"password\""
        search = password.find("123")
        assert search < 0, "Password shouldn't contain \"123\""
        break
    except AssertionError as e:
        print(f"{e}. Try Again!")
