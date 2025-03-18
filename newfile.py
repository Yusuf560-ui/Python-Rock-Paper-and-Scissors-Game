# Prompt the players to pick btwn Rock, Paper n Scissors
# Computer picks
# Record computer wins and player wins

import random
    
def play():
    computer_score = 0
    player_score = 0
    options = ["rock", "paper", "scissors"]

    while True:
        print()
        player_move = input("Pick between (rock / paper / scissors  q-quit) : ").lower()
        while player_move not in options and player_move != "q":
            print("Invalid choice")
            player_move = input("Pick between (rock / paper / scissors q-quit): ").lower()
        
        if player_move == "q":
            print("---Goodbye---")
            break
        
        if player_move in options:
            # 0-rock     1-paper      2-scissors
            computer_move = options[random.randint(0, 2)]
            print(f"You picked {player_move} -------- computer picked {computer_move}")
  
            # Checking for wins
            if (player_move == "rock" and computer_move == "scissors") or \
               (player_move == "paper" and computer_move == "rock") or \
               (player_move == "scissors" and computer_move == "paper"):
                print("---You win---")
                player_score += 2
            
            elif player_move == computer_move:
                print("---Tie---")
            
            else:
                computer_score += 2
                print("---You lose---")
            print(f"Your score : {player_score}      |       Computer score: {computer_score}")
print("-------Welcome to EasyPy Rock, Paper, and Scissors Game-------")

playing = input("Do you want to play ? (y-yes / n-no) ").lower()
while playing not in ["y", "n"]:
    print("Invalid choice, \nKindly choose y to play / n-no")
    playing = input("Do you want to play ? (y-yes / n-no) ")

if playing == "y":
    play()