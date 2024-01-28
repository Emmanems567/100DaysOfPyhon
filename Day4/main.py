import random

# result = random.randint(0, 1)

# if result == 0:
#     print("Tails")
# elif result == 1:
#     print("Heads")

#===============================

# names_string = input()

# names = names_string.split(", ")

# result = random.randint(0, len(names) - 1)

# print(f"{names[result]} is going to buy the meal today")

#===============================

# line1 = ["■", "■", "■"]
# line2 = ["■", "■", "■"]
# line3 = ["■", "■", "■"]

# map = [line1, line2, line3]

# position = input("Enter where you want to burry the treasure: ")

# x = position[0]
# y = position[1]

# if x == "A":
#     n = 0
# if x == "B":
#     n = 1
# if x == "C":
#     n = 2

# if y == "1":
#     m = 0
# if y == "2":
#     m = 1
# if y == "3":
#     m = 2

# map[m][n] = "X"

# print(f"{line1}\n{line2}\n{line3}")

#===============================

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

options = [rock, paper, scissors]

human = int(input("What do you choose? [0]Rock [1]Paper [2]Scissors "))

print(options[human])

computer = random.randint(0, 2)

print("Computer chooses: ")
print(options[computer])

if human == computer:
    print("Draw")
elif human == 0 and computer == 1:
    print("You lose")
elif human == 0 and computer == 2:
    print("You win")
elif human == 1 and computer == 0:
    print("You win")
elif human == 1 and computer == 2:
    print("You lose")
elif human == 2 and computer == 0:
    print("You lose")
elif human == 2 and computer == 1:
    print("You win")
