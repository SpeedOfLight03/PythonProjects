import random

while True:
    roll = input("Roll the dice again[y/n]? ").lower()
    if roll == 'n':
        break
    elif roll != 'y':
        print("Enter valid choice!!")
        continue

    print(random.randrange(1, 7))
    print(random.randrange(1, 7))