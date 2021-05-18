# @Author: Jesus Gutierrez #
# @Lab: Computer Security Password Cracking #

# importing necessary libraries
import hashlib 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5

# function to attack the dictionary
def dictionary_attack(password_hash):
    # extract lines from the file
    dic = lines
    # set the variable for finding password to false at first
    pass_found = False

    # loop through the file to extract the specific word which will connect to the salt hashed value
    for word in dic:
        word = word+":U1lHiIXG:"

        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(word.encode('utf-8'))

        hashed_val = MD5.new()
        hashed_val.update(ciphertext)
        hashed_val = hashed_val.hexdigest()

        if hashed_val == password_hash:
            pass_found = True
            recovered_password = word

    # print out the adequate password that matches
    if pass_found:
        print("Your password is: {}".format(recovered_password))
    else:
        print("Password not found")

dictionary_attack("75165a572dd83de1b10b808e8ac0a905")