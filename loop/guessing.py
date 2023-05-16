import random

random_number = random.randint(1, 10)
response = "y"

while response in ["y", "n"]:
    if response == "n":
        break
    while True:
        num = int(input("Guess a number: "))
        if num == random_number:
            print("You guessed it right!")
            break
        elif num > random_number:
            print("Too high!")
        else:
            print("Too low!")
    response = input("Do you want to play again? (y/n): ")
print("Thank you for playing")
