from os import system, name
import os
import random

def clear_console():
    if name == 'nt': # for windows
        system('cls')
    else: # for mac and linux(here, os.name is 'posix')
        system('clear')

os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "YELLOW": "\033[33m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

def winner_check(move1, move2):
    print(COLOR["GREEN"])
    
    if move1 == move2:
        print("|| Thats a tie !")
        return 0
    elif move1 == "rock":
        if move2 == "scissors":
            print("|| Player_1 wins !")
            return 1
        elif move2 == "paper":
            print("|| Player_2 wins !")
            return 2
    elif move1 == "paper":
        if move2 == "scissors":
            print("|| Player_2 wins !")
            return 2
        elif move2 == "rock":
            print("|| Player_1 wins !")
            return 1
    elif move1 == "scissors":
        if move2 == "paper":
            print("|| Player_1 wins !")
            return 1
        elif move2 == "rock":
            print("|| Player_2 wins !")
            return 2
    else:
        print("** Something went wrong...!")
        return 3
    print(COLOR["ENDC"])

def play_with_hum():
    clear_console()

    print("~ Rock...")
    print("~ Paper...")
    print("~ Scissors...")
    print("* Winning score -> 3\n")
        
    player1_wins = 0
    player2_wins = 0
    winning_score = 3

    while player1_wins < winning_score and player2_wins < winning_score:
        print(COLOR["BLUE"])
        
        print(f"<< Player 1 : {player1_wins} and Player 2 : {player2_wins} >>\n")
        
        player_1 = input("Player_1 , Make your move : ").lower()
        player_2 = input("Player_2 , Make your move : ").lower()
        
        winStatus = winner_check(player_1, player_2)
        
        if winStatus == 1:
            player1_wins += 1
        elif winStatus == 2:
            player2_wins += 1
            
        print("+-----------------------------+")
            
    print(f"FINAL SCORES : Player 1 : {player1_wins} and Player 2 : {player2_wins}", COLOR["ENDC"])
    
    input("\nPress Enter to continue...")
    
def computer_move():    
    randomNumber = random.randint(0, 2)
    
    if randomNumber == 0:
        move = "rock"
    elif randomNumber == 1:
        move = "scissors"
    elif randomNumber == 2:
        move = "paper"
    else:
        move = ""
    
    return move

def play_with_com():
    clear_console()
    
    print("~ Rock...")
    print("~ Paper...")
    print("~ Scissors...")
    print("* Winning score -> 3\n")
    
    player1_wins = 0
    computer_wins = 0
    winning_score = 3

    while player1_wins < winning_score > computer_wins:
        print(COLOR["BLUE"])
        
        print(f"<< Player 1 : {player1_wins} and Computer : {computer_wins} >>\n")
        
        Player_1 = input("| Player 1 , Make Your Move : ").lower()
        Player_2 = computer_move()
        print(f"| Computer Move : {Player_2}")
        
        winStatus = winner_check(Player_1, Player_2)
        
        if winStatus == 1:
            player1_wins += 1
        elif winStatus == 2:
            computer_wins += 1
            
        print("+-----------------------------+")

    print(f"FINAL SCORES : Player 1 : {player1_wins} and Player 2 : {computer_wins}", COLOR["ENDC"])
    input("\nPress Enter to continue...")

def game_menu():
    command = "0"
    
    while command != "3":
        clear_console()
        
        print(COLOR["GREEN"], "\t|<{ Game Menu }>|\t")
        print("Choose your opponent :")
        print("1- HUMAN \n2- COMPUTER \n3- RETURN", COLOR["ENDC"])
        print("")
        
        command = input()
        if command == "1":
            play_with_hum()
        elif command == "2":
            play_with_com()
            
def info():
    print(COLOR["YELLOW"], "\t|<{ Information }>|\t\n")
    print("# Programmer -> Shima Zahabi")
    print("# Email -> shimazahabi83@gmail.com\n")
    
    print("# About Game: ")
    print("Rock, Paper, Scissors is a fun and easy hand game that anyone can learn and enjoy.")
    print("Game rule : Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("In this game, winning score is 3", COLOR["ENDC"])
    
    input("\nPress Enter to continue...")

def main():
    command = "0"
    
    while command != "3":
        clear_console()
        
        print(COLOR["BLUE"], "\t|<{ Rock Paper Scissors }>|\t")
        print("1- START A GAME \n2- INFORMATION \n3- EXIT", COLOR["ENDC"])
        
        command = input()
        if command == "1":
            game_menu()
        elif command == "2":
            info()

if __name__ == "__main__":
    main()