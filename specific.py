# @Author: Jesus Gutierrez #
# @Lab: Computer Security Password Cracking #

# importing necessary libraries
import hashlib

#Entries for user to input
password = input("Enter a password: ")

if len(password) >= 8 and len(password) <  10:
    print(password + " is a valid password")
else:
    print(password + " is not a valid password")

