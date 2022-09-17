import random

random_number = random.randint(1,10)
print("The computer has chosen a random number from 1-10. Can you guess what it is?")

num = input ("Enter a number: ")
guess = int(num)

while guess != random_number:
    if guess > random_number:
        print("Your guess is too high!")
    elif guess < random_number:
        print("Your guess is too low!")
    num = input ("Enter a number: ")
    guess = int(num)

if guess == random_number:
    print("You got it! The number was ", random_number)