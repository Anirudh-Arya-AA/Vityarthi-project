# Vityarthi-project
# Anirudh Arya
# 25BAI11192
Movie Guessing Game CLI
💡 Overview of the Project:

This project is a Command-Line Interface (CLI) game designed to test and improve movie trivia knowledge. It serves two main purposes: to provide an accessible, customizable source of entertainment for casual users, and to act as a clear, practical demonstration of fundamental Object-Oriented Programming (OOP) principles in Python. The application manages session state (score, streaks) and implements algorithmic logic for title obfuscation and hinting without requiring any external dependencies.

✨ Key Features
The game offers dynamic and interactive features:

Custom Knowledge Base: Users define the game content by inputting a dynamic list of movies (the "Knowledge Base") at the start of each session.

Dynamic Difficulty: Players select from Easy, Medium, or Hard settings. This choice dictates the percentage of letters hidden in the title and applies a corresponding score multiplier.

Point-Deducting Hint System: Players can type the keyword HINT during gameplay to reveal one hidden letter, which results in a fixed 5-point deduction from their current score.

Score and Streak Tracking: The system accurately tracks the total score across all rounds, the number of rounds played, and maintains a counter for the player's longest consecutive correct guess streak.

🛠️ Technologies/Tools :
The project is built for maximum accessibility and portability, relying only on standard Python libraries.CategoryItemDescriptionLanguagePython 3.xThe core programming language used.LibrariesrandomUsed for selecting movies and determining which letters to hide.LibrariestimeA standard library used for any necessary timing or delays (often used for user experience).ArchitectureObject-Oriented (OOP)Built around a class (e.g., MovieGame) to manage session state and game logic.

⬇️ Steps to Install & Run the Project
Since the project uses only standard libraries, installation is minimal.

Save the Code: Copy the entire Python script and save it locally as a file named movie_game.py.

Open Terminal: Open your operating system's terminal or command prompt.

Navigate: Navigate to the directory where you saved movie_game.py.

Execute the Script: Run the following command to start the game:
🧪 Instructions for Testing
Follow these steps to quickly verify the core gameplay mechanics and features:

Start the Game: Run the script using python movie_game.py.

Setup & Customization Test:

Input a list of 3-4 movies when prompted (e.g., Jaws, Aliens, Predator).

Select difficulty 3 (Hard) to test the highest score multiplier and obfuscation level.

Hint System Test:

When the first mystery title appears, type HINT.

Verify: 5 points are deducted from the score, and one hidden letter is revealed in the title.

Score Multiplier Test:

Correctly guess the next movie.

Verify: The score increases significantly due to the Hard difficulty's score multiplier.

Exit Test:

After the round, when prompted Play again? (y/n):, type n.

Verify: The FINAL STATS screen appears, and the script terminates successfully.

<img width="866" height="507" alt="Screenshot 2025-11-24 000502" src="https://github.com/user-attachments/assets/8e0d103f-bfec-4000-962f-e93022abed08" />
<img width="867" height="607" alt="Screenshot 2025-11-24 000526" src="https://github.com/user-attachments/assets/203b5bae-4111-4c54-b85e-42af4f86390b" />
<img width="859" height="305" alt="Screenshot 2025-11-24 000540" src="https://github.com/user-attachments/assets/7772d767-fb9c-43d5-8afe-0f03b60a2224" />
<img width="878" height="425" alt="Screenshot 2025-11-24 000551" src="https://github.com/user-attachments/assets/6b322280-d92b-491b-b9ab-3a05bd82ae3b" />
<img width="855" height="610" alt="Screenshot 2025-11-24 000607" src="https://github.com/user-attachments/assets/682c3719-b517-46e6-8720-7e7372b0db42" />






