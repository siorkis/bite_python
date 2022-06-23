import random

with open('sowpods.txt') as s:
    words = [line[:-1] for line in s]

word = random.choice(words)
answer = []
game_word = []
guess_left = 6

for char in word:
    answer.append(char)

for i in range(len(word)):
    game_word.append('_')

man = [    'O',
      '-' ,'||', '-',
        '| ', '| ']

def print_man(man):
    for j in range(len(man)):
        if j == 0:
            print('   '+ man[j], end=' ')
        elif j == 1:
            print()
            print(man[j], end=' ')
        elif j == 4:
            print()
            print(' ' + man[j], end=' ')
        else:
            print(man[j], end=' ')

print(word)
print(answer)
print_man(man)

while True:
    print()
    start = input("Start a new game? (yes):\n")

    if start == "yes":
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
                guess_left -= 1
                man.pop(-1)
                print_man(man)
                print()
                # print("\nRemain", guess_left, "attempts")
                if guess_left == 0:
                    print("You loose")
                    break

            # print guessing word
            for char in game_word:
                print(char, end=' ')
            print()
    else:
        break

