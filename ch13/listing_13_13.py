"""
Более сложная программа `echo`
"""
import time
from random import randrange

user_input = ""

while user_input != "quit":
    user_input = input("Enter text ('quit' to exit): ")
    for i in range(randrange(10)):
        time.sleep(0.5)
        print(user_input)
