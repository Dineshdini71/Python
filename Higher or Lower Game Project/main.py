from art import logo , vs
from game_data import data
import random

def formate_data(account):
    """ Formate the account data in a printable formate"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_desc}, from {account_country}'
def check_answer(user_guess, a_account, b_account):
    if a_account > b_account:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    # Generate a random account the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {formate_data(account_a)}")
    print(vs)
    print(f"Against B: {formate_data(account_b)}")

    # Ask us to user guess who has more followers

    guess = input('who has more followers? Type A or B: ').lower()

    print('\n' * 20)
    print(logo)
    # check if user is correct
    #   - Get follower from each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"you're right! Current score {score}")
    else:
        print(f"Sorry! that's wrong. Final score: {score}")
        game_should_continue = False
    






