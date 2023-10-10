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

#Write your code below this line 👇
symbols = [rock, paper, scissors]
import random

computer = str(random.randint(0, 2))
player = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

# Invalid input
if int(player) >= 3 or int(player) < 0:
  print('you chose an invalid input, you lose!')
else:
  print(symbols[int(player)])
  print('computer chose:')
  print(symbols[int(computer)])

# draw
if computer == player:
    print("It's a draw!")

# combo
combo = player + computer

# make winning list
win_combos = ['02', '10', '21']

# check wins
if combo == win_combos[0] or combo == win_combos[1] or combo == win_combos[2]:
    print('you win!')
else:
    print('you lose!')
