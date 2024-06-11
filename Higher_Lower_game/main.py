import random
import os
from art import logo, vs
from game_data import data
def random_account():
    return random.choice(data)
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, {country}"
def check_score(guess, a_follwers, b_followers):
    if a_follwers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
def game():
    print(logo)
    score=0
    game_should_continue = True
    account_a = random_account()
    account_b = random_account()
    while game_should_continue:
        account_a = account_b
        account_b = random_account()
    while account_a == account_b:
        account_b = random_account()
    print(f"Compare A: {format_data()}")
    print(vs)
    print(f"Against B: {format_data()}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_score(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print(logo)
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
game()
    
