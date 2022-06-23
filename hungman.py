import random

with open('sowpods.txt') as s:
    words = [line[:-1] for line in s]

word = random.choice(words)
answer = []
game_word = []
fail = 0

for char in word:
    answer.append(char)

for i in range(len(word)):
    game_word.append('_')

print(word)
print(answer)

while True:
    letter = input("Guess the letter:\n")
    letter = letter.upper()

    if letter in game_word:
        print("You have already found that letter, try another:\n")
    elif letter in answer:
        indices = [i for i, x in enumerate(answer) if x == letter]
        for index in indices:
            game_word[index] = letter
        if answer == game_word:
            for char in game_word:
                print(char, end=' ')
            print("\nYou won")
            break
    else:
        print("There are no such letter, try again:\n")
        fail += 1
        print("Remain", 6-fail, "attempts")
        if fail == 6:
            print("You loose")
            break

    # print guessing word
    for char in game_word:
        print(char, end=' ')
    print()
