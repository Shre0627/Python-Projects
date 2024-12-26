# Shreya Jamnadas
# December 26 2024
# Creating a Password Validator Program, Palindrome Program, and Guess Number Game
# Next Steps:

# Password Validator - Requirements: Password Legnth should be between 8-20
# password should contain a lowercase letter, upercase letter, digit, and special character
# should not be a simple sequence and shouldn't include the username or part of the username, and no spaces
"""
Basic Requirements for the Password:
Length:

Minimum and maximum length (e.g., password should be at least 8 characters long and no more than 20 characters).
Character Types:

The password should contain at least one lowercase letter (a-z).
The password should contain at least one uppercase letter (A-Z).
The password should contain at least one numerical digit (0-9).
The password should contain at least one special character (e.g., !, @, #, $, %, etc.).
No Common Words or Sequences:

The password should not be a simple sequence (e.g., 1234, abcd, password).
The password should not include the username or parts of the user’s email address (optional for added security).
No Spaces:

Passwords should not contain spaces.
"""

# function for each checker

def isDigitCheck(pw):
    for x in pw:
        if isinstance(x, (int)):
            return True

def lettersCheckUpper(pw):
    for x in pw:
        letter = x.isupper()
        if letter:
            return True

def lettersCheckLower(pw):
    for x in pw:
        letter = x.islower()
        if letter:
            return True
            
def specialCharCheck(pw):
    for x in pw:
        if x == "@" or x == "$" or x == "#" or x == "!" or x == "%":
            return True

username = input("Enter your username: ")
password = input("Enter your password: ")

if len(password) >= 8 and len(password) <= 20:
    if isDigitCheck(password) and lettersCheckLower(password) and lettersCheckUpper(password) and specialCharCheck(password):



