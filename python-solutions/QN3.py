#Write a program that generates a random number between 1 and 10 and then asks the user to guess what the number is. The program should then tell the user whether their guess was too high , too low, or correct.

import random
Cnumber = random.randrange(1, 10)
userNumber = int(input("Enter a number between 1 and 10: "))

if userNumber>Cnumber:
    print("Computer Number!",Cnumber)
    print(f"Your guess number {userNumber} is too high")
elif Cnumber>userNumber:
    print("Too low!", Cnumber)
    print(f"Your guess number {userNumber} is too low")
else:
    print("Correct!",Cnumber)
    print(f"Your Guess Number {userNumber} is Correct!")

