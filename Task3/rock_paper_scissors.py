# Rock-Paper-Scissors Game - Certura Internship Task 3
# Author: Muzamal Asghar
# Date: August 14, 2025
# Objective: CLI game vs computer with scoring.
# Usage: Enter choices, q to quit.
# Details: Random AI, conditionals, loop.

import random

CHOICES = ['rock', 'paper', 'scissors']

def get_player_choice():
    """
    Validate choice.
    """
    while True:
        choice = input("Enter choice (rock/paper/scissors) or 'q': ").lower()
        if choice in CHOICES or choice == 'q':
            return choice
        print("Invalid.")

def get_computer_choice():
    """
    Random AI.
    """
    return random.choice(CHOICES)

def determine_winner(player, computer):
    """
    Apply rules.
    """
    if player == computer:
        return 'tie'
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'scissors' and computer == 'paper') or \
       (player == 'paper' and computer == 'rock'):
        return 'player'
    return 'computer'

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors! 🎮")
    player_score = 0
    computer_score = 0
    while True:
        player_choice = get_player_choice()
        if player_choice == 'q':
            break
        computer_choice = get_computer_choice()
        print(f"Computer: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            print("You win! 🏆")
            player_score += 1
        elif winner == 'computer':
            print("Computer wins! 🤖")
            computer_score += 1
        else:
            print("Tie! 🤝")
        print(f"Scores: You {player_score} | Computer {computer_score}\n")
    print(f"Game over! You {player_score} | Computer {computer_score} 🚀")