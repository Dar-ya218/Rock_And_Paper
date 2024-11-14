import random
import time

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    return "player" if winning_combinations[player] == computer else "computer"

def display_ascii_art(choice):
    art = {
        'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        'paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    }
    print(art[choice])

# Game stats
player_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
print("Can you defeat the mighty AI? (Spoiler: It's just random.choice) 😉")

while True:
    print("\n🏆 Score - You:", player_score, "| Computer:", computer_score)
    print("\nChoose your weapon:")
    print("1. 🪨 Rock")
    print("2. 📄 Paper")
    print("3. ✂️ Scissors")
    print("4. 🚪 Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == '4':
        print("\n🎭 Thanks for playing! Come back when you're ready for more!")
        break
        
    if choice not in ['1', '2', '3']:
        print("🚫 Hey, that's not a valid move! Try again!")
        continue
    
    # Convert choice to weapon
    weapons = {
        '1': 'rock',
        '2': 'paper',
        '3': 'scissors'
    }
    
    player_choice = weapons[choice]
    computer_choice = get_computer_choice()
    
    print("\n🎭 Your choice:")
    display_ascii_art(player_choice)
    
    print("🤖 Computer thinking", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    print("Computer's choice:")
    display_ascii_art(computer_choice)
    
    result = get_winner(player_choice, computer_choice)
    
    if result == "tie":
        print("🤝 It's a tie! Great minds think alike!")
    elif result == "player":
        print("🎉 You win! You're clearly a pro at this!")
        player_score += 1
    else:
        print("💔 Computer wins! Don't worry, it's probably cheating!")
        computer_score += 1