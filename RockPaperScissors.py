import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Combine ASCII art into list
rps = [rock, paper, scissors]

# Get input choice, convert to an integer
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for Scissors.\n"))
# Print choice from ASCII list
if choice >= 3 or choice < 0:
  print("Invalid entry, you lose!")
else:
  print(rps[choice])

  # Generate Pseudo Random Number
  oppchoice = random.randint(0, 2)
  
  # Print choice from ASCII list
  print("The computer chose")
  print(rps[oppchoice])
  
  # Win / Loss Scenarios
  if choice == oppchoice:
    print("It's a draw!")
  elif choice == 0 and oppchoice == 2:
    print("You win!")
  elif choice == 2 and oppchoice == 0:
    print("You lose!")
  elif choice < oppchoice:
    print("You lose!")
  elif  choice > oppchoice:
    print("You win!")