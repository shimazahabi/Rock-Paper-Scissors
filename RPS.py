from os import system, name
import os
import random

def clearConsole():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
def pressKey():
    input("\nPress Enter to continue...")

os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "YELLOW": "\033[33m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

def winnerCheck(move1, move2):
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

def playWithHum():
    clearConsole()

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
        
        Player_1 = input("Player_1 , Make your move : ").lower()
        Player_2 = input("Player_2 , Make your move : ").lower()
        
        winStatus = winnerCheck(Player_1, Player_2)
        
        if winStatus == 1:
            player1_wins += 1
        elif winStatus == 2:
            player2_wins += 1
            
        print("+-----------------------------+")
            
    print(f"FINAL SCORES : Player 1 : {player1_wins} and Player 2 : {player2_wins}", COLOR["ENDC"])
    
    pressKey()
    
def computerMove():    
    randomNumber = random.randint(0, 2)
    move = ""

    if randomNumber == 0:
        move = "rock"
    elif randomNumber == 1:
        move = "scissors"
    elif randomNumber == 2:
        move = "paper"
    
    return move

def playWithCom():
    clearConsole()
    
    print("~ Rock...")
    print("~ Paper...")
    print("~ Scissors...")
    print("* Winning score -> 3\n")
    
    player1_wins = 0
    computer_wins = 0
    winning_score = 3

    while player1_wins < winning_score and computer_wins < winning_score:
        print(COLOR["BLUE"])
        
        print(f"<< Player 1 : {player1_wins} and Computer : {computer_wins} >>\n")
        
        Player_1 = input("| Player 1 , Make Your Move : ").lower()
        Player_2 = computerMove()
        print(f"| Computer Move : {Player_2}")
        
        winStatus = winnerCheck(Player_1, Player_2)
        
        if winStatus == 1:
            player1_wins += 1
        elif winStatus == 2:
            computer_wins += 1
            
        print("+-----------------------------+")

    print(f"FINAL SCORES : Player 1 : {player1_wins} and Player 2 : {computer_wins}", COLOR["ENDC"])
    pressKey()

def gameMenu():
    command = "0"
    
    while command != "3":
        clearConsole()
        
        print(COLOR["GREEN"], "\t|<{ Game Menu }>|\t")
        print("Choose your opponent :")
        print("1- HUMAN \n2- COMPUTER \n3- RETURN", COLOR["ENDC"])
        
        command = input()
        if command == "1":
            playWithHum()
        elif command == "2":
            playWithCom()
            
    
def info():
    print(COLOR["YELLOW"], "\t|<{ Information }>|\t\n")
    print("# Programmer -> Shima Zahabi")
    print("# Email -> shimazahabi83@gmail.com\n")
    
    print("# About Game: ")
    print("Rock, Paper, Scissors is a fun and easy hand game that anyone can learn and enjoy.")
    print("Game rule : Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("In this game, winning score is 3", COLOR["ENDC"])
    
    pressKey()

def mainMenu():
    command = "0"
    
    while command != "3":
        clearConsole()
        
        print(COLOR["BLUE"], "\t|<{ Rock Paper Scissors }>|\t")
        print("1- START A GAME \n2- INFORMATION \n3- EXIT", COLOR["ENDC"])
        
        command = input()
        if command == "1":
            gameMenu()
        elif command == "2":
            info()

mainMenu()