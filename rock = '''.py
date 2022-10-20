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


chose = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
players_Choice = int(chose)
if players_Choice == 0:
    print(rock)
elif players_Choice == 1:
    print(paper)
elif players_Choice == 2:
    print(scissors)

print("Computers choice: ")
computers_Choice = random.randint(0,2)
if computers_Choice == 0:
    print(rock)
elif computers_Choice == 1:
    print(paper)
elif computers_Choice == 2:
    print(scissors)

if players_Choice == computers_Choice:
    print("It's a draw!")

if players_Choice == 0 and computers_Choice == 1:
    print("Paper beats rock, you lose")
elif players_Choice == 0 and computers_Choice == 2:
    print("Rock beats scissors, you win") 

if players_Choice == 1 and computers_Choice == 0:
    print("Paper beats rock, you win")
elif players_Choice == 1 and computers_Choice == 2:
    print("Scissors beats paper, you lose")

if players_Choice == 2 and computers_Choice == 0:
    print("Rock beats scissors, you lose")
elif players_Choice == 2 and computers_Choice == 1:
    print("Scissors beats paper, you win")

