import random


rock = 1
scissors = 2
paper = 3
wins = 0
loses = 0
tied = 0
rounds = 0

# function to get random choice from computer player (1, 2, 3) 
def get_computer_choice():
    return random.randint(1, 3)

while True:
    while True: 
        print("Welcome to Rock, Scissors, Paper Game")
        print("1*_Play Game")

        print("2*_Quit Game")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            print("Let's play")
            break
        elif choice == 2:
            print("Goodbye")
            exit()
        else:
            print("Invalid input. Please try again")
            continue

    while True:
        print("Please enter your choice")
        print("1. rock")
        print("2. scissors")
        print("3. paper")
        player1 = int(input("Player 1, please enter your choice: "))
        if player1 == 1:
            print("Player 1 chose rock")
        elif player1 == 2:
            print("Player 1 chose scissors")
        elif player1 == 3:
            print("Player 1 chose paper")
        else:
            print("Invalid input. Please try again")
            continue

        player2 = get_computer_choice()

        if player1 == 2 and player2 == 1:
            print("Player 1 loses")
            print("Player 2 chose rock")
            print("rock beats scissors")
            loses += 1
        elif player1 == 2 and player2 == 3:
            print("Player 1 wins")
            print("Player 2 chose paper")
            print("scissors beats paper")
            wins += 1
        elif player1 == 1 and player2 == 2:
            print("Player 1 wins")
            print("Player 2 chose scissors")
            print("rock beats scissors")
            wins += 1
        elif player1 == 1 and player2 == 3:
            print("Player 1 loses")
            print("Player 2 chose paper")
            print("paper beats rock")
            loses += 1
        elif player1 == 3 and player2 == 1:
            print("Player 1 wins")
            print("Player 2 chose rock")
            print("paper beats rock")
            wins += 1
        elif player1 == 3 and player2 == 2:
            print("Player 1 loses")
            print("Player 2 chose scissors")
            print("scissors beats paper")
            loses += 1
        elif player1 == player2:
            print("Player 1 and Player 2 tied")
            tied += 1

        print("Do you want to play again?")
        rounds += 1
        print("1. Yes")
        print("2. No")
        answer = int(input("Please enter your choice: "))
        if answer == 1:
            continue
        elif answer == 2:
            print("Results: rounds:",rounds, " wins:",wins, "loses:",loses, "tied:",tied);
            break
        else:
            print("Invalid input. Please try again")
            continue

   