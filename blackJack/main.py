import random
from logging import fatal

from art import logo

print(logo)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # if 11 in cards and 10 in cards and len(cards) == 2:
    # instead writing this follow below method
    """Take a list of cards and return the score of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🤝"
    elif c_score == 0:
        return "Lose, opponent has blackjack"
    elif u_score == 0:
        return "Win 🥇 computer has blackjack"
    elif u_score > 21:
        return "Lose the Game 😔"
    elif c_score > 21:
        return "Win the game 😀, bcz 🖥️ has over 21"
    elif u_score > c_score:
        return "You Win 🏆"
    else:
        return "You Lose 😓"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_gameover = False

    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 and computer_score == 0 and computer_score > 21:
            is_gameover = True
        else:
            user_should_deal = input("Continue Type 'Y' or Type No 'N' to discontinue ")
            if user_should_deal == 'Y' or user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"---------USER SCORE---------->[ {user_score} ]-----------")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"---------COMPUTER SCORE-------->[ {computer_score} ]---------")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Play the game again Type 'Y' for yes and Type 'N' for NO "):
    print('/n' * 20)
    play_game()

