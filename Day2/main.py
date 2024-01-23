# num = input()

# char = str(num)

# a = int(char[0])
# b =  int(char[1])

# print(result = a + b)

#========================

# height = float(input())
# weight = int(input())

# bmi = (weight / (height ** 2))

# print(int(bmi))

#========================

# age = int(input())

# time_left = 90 - age

# weeks_left = time_left * 52

# print(f"You have {weeks_left} left.")

#========================

print("Welcome to the tip calculator v5.67.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_per = percentage / 100 + 1

tip = (bill * total_per) / people

print(f"Each person should pay: ${round(tip, 2)}")

