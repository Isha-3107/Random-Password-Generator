# random password generator
import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
length = int(input("Enter the length of the password: "))
a = "".join(random.sample(password, length))
print(f"Your password is: {a}")
