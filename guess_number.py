import random
from replit import clear

num =0
def choose_number():
  global num
  num = random.randint(1, 100)
  print(num)


#function to choose a level and the no of attempts
def choose_level():
  game_level = input("\nChoose the level of difficulty: \n\t1. Easy\n\t2. Medium\n\t3. Hard\n\n-> ")
  if game_level == "Easy" or game_level == "easy":
    chances = 10
    return chances
  elif game_level == "Medium" or game_level == "medium":
    chances = 8
    return chances
  elif game_level == "Hard" or game_level == "hard":
    chances = 5
    return chances
  
#function to check if the user guesses the correct answer or not
def check_guess(guess):
  if guess>num:
    return 0
  elif guess<num:
    return 1
  elif guess==num:
    return 2

#driver game code
player_ans = "yes"
while player_ans=="yes":
  clear()
  choose_number()
  no_of_chances = choose_level()
  i = no_of_chances
  while i>0:
    print(f"\nYou have {i} attempts remaining to guess the number.")
    guess = int(input("Make a guess:  "))
    status = check_guess(guess)
    
    if status == 0:
      print("Too high. Guess again\n")
      i -=1
    elif status == 1:
      print("Too low. Guess again.\n")
      i -=1
    elif status == 2:
      print(f"You got it! The answer was {guess}")
      i = 0
    
  player_ans = input("\nWould you like to play again?   ")
