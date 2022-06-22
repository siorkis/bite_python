import random

number = random.randint(1000, 9999)
number_array = [int(x) for x in str(number)]

while True:
    count_cow = 0
    count_bull = 0
    guess = int(input("Guess the number:\n"))
    guess_array = [int(x) for x in str(guess)]

    if guess == number:
        print("You won")
        break

    for i in range(len(number_array)):
        if number_array[i] == guess_array[i]:
            count_cow += 1

    for i in range(len(guess_array)):
        if guess_array[i] in number_array and guess_array[i] != number_array[i]:
            count_bull += 1

    print(count_cow, " cows,", count_bull, " bulls")
