Problem #1

a.	The attributes that are stored for an individual user in a shadow file are:
  i.	Username
  ii.	Encrypted password
  iii.	Date of last password change
  iv.	Minimum required days between password changes
  v.	Maximum required days between password changes
  vi.	Number of days in advance to display password expiration
  vii.	Number of days after password expiration to disable account
  viii.	Account expiration date
  ix.	Reserve field
b.	All local user account passwords in a Windows system are located inside:
  i.	C:\windows\system32\config\SAM
c.	Python program:
  a.	Able to hash string passwords given from the “commonPasswdFile.txt”
d.	Able to crack 197 passwords out of 200 from the “shadowfile.txt”
e.Able for program to output all the username combinations after successful crack and also able to verify with UTEP VPN log in: 
  i. Command to run the python program “main.py” shown below
  ii. main.py commonPasswdFile.txt shadowfile.txt resultd.txt
  iii.this will read both files, compare them, and then create a new file names “result.txt” with the passwords in order
f.	Algorithm only successful by cracking a salted hash given a specific hash and also a given salt by using a dictionary. This was the only way I was able to implement the algorithm. Strictly attaching the salt to the word, encrypting it, and finally hashing it.

g.	First tried a reverse approach to see if my algorithm works or if there is something wrong:
  i.	Picked a password
  ii.	Salted the password
  iii.	Obtained the hash
  iv.	Generate some small list with that password
  v.	Feed the created list and the hash to my function to see if it works correctly


