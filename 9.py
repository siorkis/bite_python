import random

number = random.randint(1, 9)
guesses = 0

while True:
    stop = input("Input your number (say exit to quit)\n")
    guesses += 1
    if stop == 'exit':
        break
    if int(stop) > number:
        print("Number is lower")
    elif int(stop) < number:
        print("Number is higher")
    elif int(stop) == number:
        print("You are right")
        print("Number of guesses =",guesses)
        break
