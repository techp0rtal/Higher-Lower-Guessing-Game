from art import logo, vs
from game_data import data
import random

"""
 For this project we will think of it as a game with turns. Every turn has 9 parts:
 1. randomly select keys from dictionary. remove those two from the dataset
 2. print all the text to the console
 3. get input from user. --> if it's not right input it's wrong. if you get all 50 you win
 4.make a new dictionary with the current candidate, and its values. 
 5. compare the candidates' values. what is the right answer? a b, 
 6. reset the current candidate dictionary, but keep one of them the same. --> REMOVE the old one from the list.
 7.if right Adjust the score and print new line, if wrong, clear all except the logo and print sorry, that's wrong .
 8. check 'still_playing' status
 9. if so, repeat.
 (Bonus)10. if you get it right 49 times (or if the list of candidates == 0)....you win!
 See the flowchart I included for a more visual representation of the above logic.
 """

def print_correct(new_score):
    print(logo)
    print(f"You're right! Current score: {new_score}")
    print(f"Compare A: {option_A["name"]}, a {option_A["description"]}, from {option_A["country"]}")
    print(vs)
    print(f"Against B: {option_B["name"]}, a {option_B["description"]}, from {option_B["country"]}")

def select_candidate():
    new_candidate = random.choice(data)
    return new_candidate


print(logo)
score = 0
option_A, option_B = random.sample(data, 2)
print(f"Compare A: {option_A["name"]}, a {option_A["description"]}, from {option_A["country"]}")
print(vs)
print(f"Against B: {option_B["name"]}, a {option_B["description"]}, from {option_B["country"]}")


while True:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    correct_answer = ""
    if option_A["follower_count"] > option_B["follower_count"]:
        correct_answer = "A"
    else:
        correct_answer = "B"


    if user_choice == correct_answer:
        print("\n" * 20)
        score += 1
        option_A = option_B
        option_B = select_candidate()
        print_correct(score)

    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break







# If I were to recreate the game, so the same one couldn't be picked I would change it to be like this:
# def select_candidate(loser):
#     global data
#     data.remove(loser)
#     new_candidate = random.choice(data)
#     return new_candidate
#I would also make it to where you can BEAT the game by guessing more than 49 times. if correct, remove that dictionary from the list until the list eventualyl reaches 0.
# make the main game loop say: while still_playing == True and len(data) > 0:
#     print(f"You're right! Current score: {score}.")
#     if len(data) == 0:
#         print("You beat the game! Congratulations")
#         break
# data.remove(option_A), data.remove(
#     option_B)  # this ensures that from now on, we won't randomly select the same one since we will use random.choice -- which doesn't guarantee a unique value
# I would also keep a high score somewhere. and ask to try again.