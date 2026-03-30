import sys
import random
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "enter...\n1 for rock \n2 for paper or \n3 for scissors:\n\n")

    if playerChoice not in ['1', '2', '3']:
        print("invalid input, you must enter 1, 2 or 3")
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice('123')

    computer = int(computerChoice)

    print("you chose: " + str(RPS(player)).replace("RPS.", "").title() + ".")
    print("computer chose: " + str(RPS(computer)
                                   ).replace("RPS.", "").title() + ".")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"
    result = decide_winner(player, computer)
    print(result)

    global game_count
    game_count += 1

    print("\nGames played: " + str(game_count))

    print("\nDo you want to play again?")

    while True:
        playagain = input("\nY for Yes or \nQ to quit:\n\n")
        if playagain.lower() == ['y', 'q']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
