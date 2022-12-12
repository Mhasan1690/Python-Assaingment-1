
play = [ "Rock", "Paper", "Scissors" ]

player = int(input('Enter your selection!'))

computer = 
if player == "Rock":
    print('You chose Rock')
elif player == "Paper":
    print('You chose Paper')
else:
    print('You chose Scissors')
if player == computer:
    print("Tie")
elif player == "Rock":
    if computer == "Paper":
        print (" You Lose The Game")
    else:
        print(" You Won The Game")

elif player == "Paper":
    if computer == "Scissors":
        print (" You Lose The Game")
    else:
        print(" You Won The Game")       

elif player == "Scisoors":
    if computer == "Rock":
        print (" You Lose The Game")
    else:
        print(" You Won The Game")