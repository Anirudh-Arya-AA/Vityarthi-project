# Vityarthi-project
# Anirudh Arya
#25BAI11192
Movie Guessing Game CLI
Overview of the Project
This project is a simple, Command-Line Interface (CLI) game designed to test a player's knowledge of movie titles. The player inputs a list of movies, chooses a difficulty level, and then attempts to guess the titles after some letters have been obscured by a placeholder character. The game tracks scores, tracks streaks, and includes a point-deducting hint system.

Features
Custom Knowledge Base: The game begins by letting the user input a list of movies (the knowledge base).

Difficulty Scaling: The amount of obfuscation (hidden letters) is adjusted based on the chosen difficulty (Easy, Medium, Hard).

Score Multipliers: Difficulty choice affects the points earned for a correct guess.

Hint System: Players can type HINT to reveal a random hidden letter, which costs 5 points.

Persistence: The game runs continuously, allowing the player to play multiple rounds until they choose to QUIT or type 'n' to stop playing.

Statistics Tracking: The final score, total rounds played, correct guesses, and best streak are displayed upon quitting.

Technologies/Tools Used
Programming Language: Python 3.x

Standard Libraries:

random: Used for selecting random movies and choosing which letters to obscure or reveal for hints.

time: Used for small delays to enhance the user experience (UX) pacing.

Steps to Install & Run the Project
This project uses only Python's standard library and requires no external installation.

Save the Code: Copy the code into a file named movie_game.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:

Bash

python movie_game.py
Instructions for Testing
Follow these steps to ensure all major features of the game are functioning correctly:

Initial Setup:

When prompted for movies, enter a short list, e.g., Jaws, Aliens, Terminator.

When prompted for the placeholder, try entering a different character, like #.

Difficulty Test: Select 3 for Hard difficulty (to ensure max obfuscation).

Gameplay Loop Test:

The game should display >>> ROUND 1 <<<.

Test Guessing: Guess one of the movies correctly (e.g., Aliens). Verify the score increases and streak starts.

Test Hint Cost: Play the next round. Type HINT. Verify the score decreases by 5 points and one hidden character is revealed.

Test Error Messages: Type an invalid difficulty choice (e.g., 9) and verify the message ?? try again appears.

Test Failures: Attempt to guess a movie wrong three times. Verify the round ends with the message no tries left and streak resets to 0.

Exit Test: When asked again? (y/n):, type n. Verify the FINAL STATS screen appears before the program exits with ok done.
