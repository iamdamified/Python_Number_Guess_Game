import time
import random


# random.choice()
# range(0, 10)

your_name = (input("Welcome to Guess game, please enter your name below: \n"))

def guessGame(n):
    player_score = 0
    system_score = 0
    number_guess = int(input("Dear " + your_name + " enter a number between 0 to 9: \n"))
    system_guess = random.randrange(0, 10)
    for i in range(0, 5):
            if system_guess != number_guess:
                  system_score += 1
                  print(f" system played: {system_guess} ... Please wait..\n")
                  time.sleep(4)
                  print(f"system {system_score}, player {player_score}.")
                  number_guess = int(input("Enter a new number between 0 to 9: \n"))
                  system_guess = random.randrange(0, 10)
            else:
                  player_score += 1
                  print(f" system played: {system_guess} ... Please wait..\n")
                  time.sleep(4)
                  print(f"system {system_score}, player {player_score}.")
                  number_guess = int(input("Enter a new number between 0 to 9: \n"))
                  system_guess = random.randrange(0, 10)
    if player_score < system_score:
          return (f"system {system_score}, player {player_score}. You lost the Game! \n try again later.")
    return (f"system {system_score}, player {player_score}. You Won!")

print(guessGame(your_name))

