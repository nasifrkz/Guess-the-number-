import random

secret_number= random.randint(1,100)

while True:
    guess = float(input("Guess the number between 1 to 100"))

    if guess == secret_number:
        print("Congrats! You guess it correctly!")
        break
    elif guess< secret_number:
        print("It will be higher!")
    else:
        print("it will be lower!")