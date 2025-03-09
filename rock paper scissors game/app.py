import random
import time
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function for animated text
def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Game options
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "✊", "paper": "📄", "scissors": "✂️"}

# Score tracking
user_score = 0
computer_score = 0

type_text(Fore.CYAN + "🎮 Welcome to Rock-Paper-Scissors Game! 🎮")
type_text("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
type_text("Type 'exit' anytime to quit.\n")

while True:
    # Get user input
    user_choice = input(Fore.YELLOW + "Your choice (rock/paper/scissors): ").lower()

    if user_choice == "exit":
        type_text(Fore.RED + "🚪 Exiting the game... Goodbye!")
        break

    if user_choice not in choices:
        type_text(Fore.RED + "⚠ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Generate computer choice
    computer_choice = random.choice(choices)

    # Display choices with emojis
    type_text(f"\nYou chose {Fore.GREEN}{user_choice.capitalize()} {emojis[user_choice]}")
    type_text(f"Computer chose {Fore.RED}{computer_choice.capitalize()} {emojis[computer_choice]}\n")

    # Determine winner
    if user_choice == computer_choice:
        type_text(Fore.BLUE + "🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        type_text(Fore.GREEN + "🎉 You win this round!")
        user_score += 1
    else:
        type_text(Fore.RED + "😢 You lose this round!")
        computer_score += 1

    # Display score
    type_text(Fore.MAGENTA + f"📊 Score: You {user_score} | Computer {computer_score}\n")

    # Ask to play again
    play_again = input(Fore.CYAN + "🔄 Play again? (yes/no): ").lower()
    if play_again != "yes":
        type_text(Fore.RED + "Thanks for playing! See you next time! 👋")
        break
