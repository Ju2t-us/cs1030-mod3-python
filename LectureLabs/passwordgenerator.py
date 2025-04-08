import random
import string

print("PASSWORD GENERATOR")
print("==================")

amount = int(input("How many passwords do you want to generate? "))
length = int(input("How long do you want the passwords to be? "))

# create a list to hold all the characters using the string library
characters = list(string.ascii_letters + string.digits + string.punctuation)

for i in range(amount):
    # create a empty variable for the password
    password = ""
    # loop through the range of the length provided above
    for j in range(length):
        # choose a random character from the list of characters and add it to the password variable
        password += random.choice(characters)
    # finally, print the password
    print(password)