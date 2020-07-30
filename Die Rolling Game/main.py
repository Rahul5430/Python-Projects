import random

x = 'y'
while x == 'y':
    number = random.randint(1, 6)
    print("~~~~~~~~~~~")
    print("|         |")
    print(f"|    {number}    |")
    print("|         |")
    print("~~~~~~~~~~~")
    x = input("Roll Again : ")
