# @Author: Jesus Gutierrez #
# @Lab: Computer Security Password Cracking #

# importing necessary libraries
import sys  # command line arguments
import os  # checking if files exist
import crypt  # crypt used to check MD5 hashes

# set input and output files
if len(sys.argv) != 4:
    print("Correct usage: main.py <dictionary text file> <shadow file text file> <output file>")
    # exit once appropriate print
    exit1 = exit()
# first file name given 'commonPasswdFile.txt'
inputFileName: str = sys.argv[1]
# second file name given 'shadowfile.txt'
inputFileName2: str = sys.argv[2]
# third file parameter 'results.txt' will be generated for passwords in order
outputFileName: str = sys.argv[3]

# verification of file given 'commonPasswdFile.txt'
if not os.path.exists(inputFileName):
    print("The text file %s doesn't exist!" % inputFileName)
    exit()
# verification of file given 'shadowfile.txt'
if not os.path.exists(inputFileName2):
    print("The text %s doesn't exist!" % inputFileName2)
    exit()

# create the array from the file 'commonPasswdFile.txt' line by line
with open(inputFileName) as my_file:
    wordArr = my_file.readlines()

# create the array from the file 'shadowfile.txt' line by line
with open(inputFileName2) as my_file:
    hashArr = my_file.readlines()

passwords = list()


# method to check for hashing
def checkhash(word, hashval):
    if hashval == crypt.crypt(word, hashval):
        return True

# method to find passwords
def findpass():
    for i in hashArr:  # 'i' stands for the hash of the first user
        i = i.strip()  # '.strip' strips the word to remove any unwanted white space
        for j in wordArr:  # 'j' stands for the word taken from a list
            j = j.strip()  # '.strip' strips the word to remove any unwanted white space
            if checkhash(j, i):
                passwords.append(j)
                break

findpass()

# 'results.txt' will be generated for passwords in order as a new text file
with open(outputFileName, "w") as outputFile:
    for item in passwords:
        outputFile.write("%s\n" % item)
