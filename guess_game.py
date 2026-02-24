import random

guess = random.randint(1, 100)



while True:
    user= int(input("Guess a number between 1 to 100:"))
    
    if user > guess:
        print("Too high! ")
    elif user < guess:
        print("Too Low!")
    elif guess == user:
        print("You Guess it right")
        break

    
    