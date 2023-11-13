import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or Scissors? [Type 'end' to end]: ").lower()

    if player == "end":
        print("\nEnding the game...")
        print(f"Your Score: {player_score}")
        print(f"Computer Score: {computer_score}")

        if player_score == computer_score:
            print("The game is a TIE!!")
        elif player_score > computer_score:
            print("Congratulations!!, You WON the Game!!")
        else:
            print("Sorry!!, You LOSE the Game!!")
        
        break
    
    print(f"Computer choice: {computer}")
    if player == computer:
        print("Tie")
    
    elif player == "rock":
        if computer == "paper":
            print("You lose!! Paper covers Rock!!")
            computer_score += 1
        else:
            print("You win!! Rock kills Scissors!!")
            player_score += 1

    elif player == "paper":
        if computer == "scissors":
            print("You lose!! Scissors cuts Paper!!")
            computer_score += 1
        else:
            print("You win!! Paper covers Rock!!")
            player_score += 1

    elif player == "scissors":
        if computer == "rock":
            print("You lose!! Rock kills Scissors!!")
            computer_score += 1
        else:
            print("You win!! Scissors cuts Paper!!")
            player_score += 1
    
    else:
        print("Enter valid choice!!")
        












