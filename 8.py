import random

player_turn = int(input("Make the choice:\n1 - paper \n2 - scissors \n3 - rock\n"))

bot_turn = random.randint(1, 3)

if player_turn == 1 and bot_turn == 3:
    print("You win, opponent's choice was",bot_turn)
elif player_turn == 2 and bot_turn == 1:
    print("You win, opponent's choice was",bot_turn)
elif player_turn == 3 and bot_turn == 2:
    print("You win, opponent's choice was",bot_turn)
elif player_turn == bot_turn:
    print("Draw")
else:
    print("You loose, opponent's choice was",bot_turn)
