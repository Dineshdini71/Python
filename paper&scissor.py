import random
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
image = [rock, scissors, paper]
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors'))
print(image[user_input])
print('Computers choices:')
computer_choice = random.randint(0, 2)
print(image[computer_choice])

if user_input >=3 or user_input < 0:
    print('You\'re entered the invalid input..! ❌')
elif user_input == 0 and computer_choice == 2:
    print('You lose..! 😔')
elif user_input == 2 and computer_choice == 0:
    print('You win..! 🥇')
elif user_input > computer_choice:
    print('You lose..! 😔')
elif user_input < computer_choice:
    print('You win..! 🥇')
elif user_input == computer_choice:
    print('Match Draws... 👥')