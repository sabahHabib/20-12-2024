# Guess the Number Game Python Project
import random
print("welcome to guess game!")
while True:
    number = random.randint(0,10)
    guess = int(input("Enter the number between:0-9)"))
    if guess == number:
        print("You win!")
    else:
        print(f"You loss the correct number was:{number} Try again!")
    play_again=input("Do you want to play again?(Yes/no):").lower()
    if play_again == "no":
        print("Good Bye!")
        break