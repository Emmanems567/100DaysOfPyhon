import random
import art
import words

word_list = words.word_list
chosen_word = random.choice(word_list)

lives = 6

stages = art.stages
logo = art.logo

print(logo)

#test
print(f"'{chosen_word}' is the solution")

display = []

for char in chosen_word:
  
  display += "_"

end_game = False

while not end_game:
  
  guess = input("Guess a letter: ").lower()

  if display.count(guess) > 0:
    
    print(f"'{guess}' is already guessed.")
    lives -= 1
  
  for n in range(len(chosen_word)):
    
    char = chosen_word[n]
    
    if char == guess: 
      
      display[n] = char
  
  if guess not in chosen_word:
    
    print(f"'{guess}' is not in the word.")
    lives -= 1
  
  print(stages[lives])

  if lives == 0:
    
    print("You lose")
    end_game = True
  
  print(f"{' '.join(display)}")

  if "_" not in display:
    
    print("You win")
    end_game = True
