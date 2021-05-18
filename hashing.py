# @Author: Jesus Gutierrez #
# @Lab: Computer Security Password Cracking #

# importing hashlib library to hash password
import hashlib
# function computes the appropriate hashing
def compute_MD5_hash(string, encoding='utf-8'):
    # hashlib library will create MD5 hash string
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()
# read file and print out the computed hash lines
with open("commonPasswdFile.txt") as f:
    for line in f:
        print(compute_MD5_hash(line))