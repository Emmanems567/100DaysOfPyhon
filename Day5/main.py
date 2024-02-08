# student_heights = input().split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# total_heights = 0

# for height in student_heights:
#     total_heights += height

# print(f"Total heigh: {total_heights}")
# print(f"Number of students: {len(student_heights)}")
# print(f"Average height: {round(total_heights / len(student_heights))}")

#=============================

# student_scores = input().split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest = 0

# for score in student_scores:
#     if score > highest:
#         highest = score
#     else:
#         score = highest

# print(f"The highest score is: {highest}")

#=============================

# target = int(input())
# total = 0

# for n in range(2, target + 1, 2):
#     total += n

# print(total)

#=============================

# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

#=============================

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []


for n in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for n in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for n in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for n in password_list:
    password += n

print(password)