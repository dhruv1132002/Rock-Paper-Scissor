import random

player_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissor"]

while True:
    player_input = input("enter Rock/Paper/Scissor to start game or Q to quit: ").lower()
    if player_input == "q":
        break
    
    if player_input not in option:
        continue
    
    randon_number = random.randint(0, 2)
    computer_picks = option[randon_number]    
    print("computer picked " + computer_picks + ". ")
        
    if player_input == "rock" and computer_picks == "scissor":
        print("player won!")
        player_wins += 1
        continue
    
    elif player_input == "paper" and computer_picks == "rock":
        print("player won!")
        player_wins += 1
        continue
    
    elif player_input == "scissor" and computer_picks == "paper":
        print("player won!")
        player_wins += 1
        continue
    
    else:
        print("you lost!")
        computer_wins += 1
        
print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
  

    