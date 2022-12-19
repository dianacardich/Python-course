#juego en python
from random import randint #random genera numeros pseudoaleatorios

choise = ["rock", "paper","scissors"]
def main():
    computer = choise[randint(0,2)] # randint genera un numero entero entre a y b, ambos incluidos, a debe ser inferior o igual a b.

    print("welcome to the Rock, Paper, Scissord Game\n")
    player = input("Your choise: ").lower()
    print("Computer Chose: " + computer)

    if player == computer: 
        print("Draw")
    elif player == "rock" and computer == "paper":
        print("Computer Wins")
    elif player == "rock" and computer == "scissors":
        print("Player Wins")
    elif player == "paper" and computer == "rock":
        print("Player Wins")
    elif player  == "paper" and computer == "scissors":
        print("Computer Wins")
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    
    main()

main()