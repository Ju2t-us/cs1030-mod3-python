import random
import string

print("PASSWORD GENERATOR")
print("==================")

amount = int(input("How many passwords do you want to generate? "))
length = int(input("How long do you want the passwords to be? "))

characters = list(string.ascii_letters + string.digits + string.punctuation)

def gen(amount, length):
    passwords = []
    for i in range(amount):
        password = ""
        for j in range(length):
            password += random.choice(characters)
        passwords.append(password)
    return passwords

print("\n".join(gen(amount, length)))