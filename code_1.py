#!/usr/bin/env python3
# Guess Game by Martoh, PLP 2024 CLASS, Kenya

import pyautogui
import random
import os

# Ensure the Scores directory exists
if not os.path.exists("Scores"):
    os.makedirs("Scores")

# Easy mode
def game_easy():
    guess = random.randint(1, 10)
    attempts = 1

    user_input = pyautogui.prompt(
        text='Guess the number between 1 and 10:',
        title='Guess Game - Easy Mode'
    )

    while user_input != str(guess):
        previous_guess = user_input
        if int(user_input) > guess:
            user_input = pyautogui.prompt(
                text=f'Try a smaller number than {previous_guess}.',
                title='Guess Game - Easy Mode'
            )
        elif int(user_input) < guess:
            user_input = pyautogui.prompt(
                text=f'Try a bigger number than {previous_guess}.',
                title='Guess Game - Easy Mode'
            )
        attempts += 1

    pyautogui.alert(
        text=f'Congratulations! You found the number in {attempts} attempts!',
        title='Guess Game - Easy Mode'
    )

    # Handle scores
    update_score("Scores/easy.txt", attempts)

    if pyautogui.confirm(text="Play again?", title="Guess Game - Easy Mode", buttons=["Yes", "No"]) == "Yes":
        game_easy()
    else:
        pyautogui.alert(text="Goodbye!", title="Guess Game")


# Medium mode
def game_medium():
    guess = random.randint(1, 50)
    attempts = 1

    user_input = pyautogui.prompt(
        text='Guess the number between 1 and 50:',
        title='Guess Game - Medium Mode'
    )

    while user_input != str(guess):
        previous_guess = user_input
        if int(user_input) > guess:
            user_input = pyautogui.prompt(
                text=f'Try a smaller number than {previous_guess}.',
                title='Guess Game - Medium Mode'
            )
        elif int(user_input) < guess:
            user_input = pyautogui.prompt(
                text=f'Try a bigger number than {previous_guess}.',
                title='Guess Game - Medium Mode'
            )
        attempts += 1

    pyautogui.alert(
        text=f'Congratulations! You found the number in {attempts} attempts!',
        title='Guess Game - Medium Mode'
    )

    # Handle scores
    update_score("Scores/medium.txt", attempts)

    if pyautogui.confirm(text="Play again?", title="Guess Game - Medium Mode", buttons=["Yes", "No"]) == "Yes":
        game_medium()
    else:
        pyautogui.alert(text="Goodbye!", title="Guess Game")


# Hard mode
def game_hard():
    guess = random.randint(1, 100)
    attempts = 1

    user_input = pyautogui.prompt(
        text='Guess the number between 1 and 100:',
        title='Guess Game - Hard Mode'
    )

    while user_input != str(guess):
        previous_guess = user_input
        if int(user_input) > guess:
            user_input = pyautogui.prompt(
                text=f'Try a smaller number than {previous_guess}.',
                title='Guess Game - Hard Mode'
            )
        elif int(user_input) < guess:
            user_input = pyautogui.prompt(
                text=f'Try a bigger number than {previous_guess}.',
                title='Guess Game - Hard Mode'
            )
        attempts += 1

    pyautogui.alert(
        text=f'Congratulations! You found the number in {attempts} attempts!',
        title='Guess Game - Hard Mode'
    )

    # Handle scores
    update_score("Scores/hard.txt", attempts)

    if pyautogui.confirm(text="Play again?", title="Guess Game - Hard Mode", buttons=["Yes", "No"]) == "Yes":
        game_hard()
    else:
        pyautogui.alert(text="Goodbye!", title="Guess Game")


# Update scores
def update_score(score_file, attempts):
    if not os.path.exists(score_file):
        with open(score_file, 'w') as file:
            file.write(str(attempts))
    else:
        with open(score_file, 'r') as file:
            best_score = int(file.read())

        if attempts < best_score:
            with open(score_file, 'w') as file:
                file.write(str(attempts))


# Mode selector
mode = pyautogui.confirm(
    text="Please select the game mode:\nEasy: 1 to 10\nMedium: 1 to 50\nHard: 1 to 100",
    title="Guess Game by Martoh - PLP 2024 CLASS",
    buttons=['Easy', 'Medium', 'Hard', 'Show Scores']
)

if mode == "Easy":
    game_easy()
elif mode == "Medium":
    game_medium()
elif mode == "Hard":
    game_hard()
else:
    # Display scores
    easy_score = open("Scores/easy.txt").read() if os.path.exists("Scores/easy.txt") else "No score"
    medium_score = open("Scores/medium.txt").read() if os.path.exists("Scores/medium.txt") else "No score"
    hard_score = open("Scores/hard.txt").read() if os.path.exists("Scores/hard.txt") else "No score"

    pyautogui.alert(
        text=f"Easy: {easy_score}\nMedium: {medium_score}\nHard: {hard_score}",
        title="Guess Game - Scores",
        buttons=["OK"]
    )
