# 1. Build a Password Generator
import random
import string

print("Welcome to Password Generator")
password_length = int(input("Please enter the length of password:"))
use_uppercase = input("include uppercase letters?(yes/no):").lower() == "yes"
use_lowercase = input("include lowercase letters?(yes/no)").lower() == "yes"
use_special_char = input("include specialchar letters?(yes/no)").lower() == "yes"
use_numbers= input("include numbers letters?(yes/no)") == "yes"
alphabet_pool=""
if use_uppercase:
    alphabet_pool+=string.ascii_uppercase
if use_lowercase:
    alphabet_pool+=string.ascii_lowercase
if use_special_char:
    alphabet_pool+=string.punctuation
if use_numbers:
    alphabet_pool+=string.digits
if not alphabet_pool:
    print("Error! at least one character type must be selected")
else:
    password = "".join(random.choice(alphabet_pool) for _ in range(password_length))
    print(password)
