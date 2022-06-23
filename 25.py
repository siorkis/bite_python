numbers = list(range(0, 101))

length = len(numbers)
index = length // 2
print(numbers[index])
guesses = 1

while True:
    answer = input("Enter lower, higher or right: (say exit to end)\n")
    if answer == "right":
        print("I found it for", guesses, "guesses")
        break
    elif numbers[index] == numbers[0] or numbers[index] == numbers[-1]:
        print("I cannot find it")
        break
    elif answer == "lower":
        index //= 2
        print(numbers[index])
        guesses += 1
    elif answer == "higher":
        index = (length - index) // 2 + index
        print(numbers[index])
        guesses += 1
    elif answer == "exit":
        break
