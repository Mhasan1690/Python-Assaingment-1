import random

Mehedi = input("Enter a choice (rock, paper, scissors): ")
possible_choices = ["rock", "paper", "scissors"]

dev_skill = random.choice(possible_choices)
print(f"\n Mehedi choose {Mehedi}, DEVSKILL choose {dev_skill}.\n")


if Mehedi == dev_skill:
      print(f"Both palyer selected{dev_skill}. It is a tie")

elif Mehedi == "rock":
    
      if dev_skill =="scissors":
            print("rock Beats Scissors. You win.")
      else:
            print("Paper Is Equal to Rock. So, You lost")


elif Mehedi == "paper":
    
      if dev_skill == "rock":
            print("Paper Beats rock. You win.")
      else:
            print("Scissors Is Equal to Paper. So, You lost")


elif Mehedi == "scissors":
    
      if dev_skill =="paper":
            print("scissors Beats rock. You win.")
      else:
            print("Rock Is Equal to Scissors. So, You lost")

 
else:
    print("That's not a valid play. Check your spelling!")