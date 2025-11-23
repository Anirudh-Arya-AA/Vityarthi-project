# Movie Guessing Game CLI : 
Project Statement
This document outlines the core aspects of the Movie Guessing Game CLI project, a text-based application designed to test movie trivia knowledge.

# 🎯 Problem Statement:

There is a need for a simple, accessible, and highly customizable movie trivia game. The solution must be a Command-Line Interface (CLI) application that requires no external dependencies or complex installation, focusing on providing entertainment while simultaneously serving as a practical, clear demonstration of fundamental Object-Oriented Programming (OOP) principles in Python.

# 🗺️ Scope of the Project:

Category	Description
IN SCOPE	CLI-based gameplay, In-Memory Data Storage (session-only), Basic Input Validation, OOP architecture (e.g., MovieGame class), and implementation of core features (difficulty, hint system, score/streak tracking).
OUT OF SCOPE	Graphical User Interfaces (GUIs), External Databases, Persistent Score Saving (scores are lost upon exit), and Multi-User Functionality.

# 👤 Target Users:

Casual Users/Movie Enthusiasts: Individuals seeking a quick, accessible, and customizable game to test their movie trivia knowledge for entertainment.

Students/Beginner Python Developers: Users interested in examining a practical, well-scoped project that clearly demonstrates core Object-Oriented Programming (OOP) concepts, state management (score, streaks), and algorithmic logic (obfuscation, hinting) in a real-world application.

# ✨ High-Level Features:

Custom Knowledge Base: Allows the user to input a dynamic list of movies at the start of the session, making the content fresh and user-defined.

Dynamic Difficulty: Players can select from Easy, Medium, or Hard settings, which determines the percentage of letters hidden in the movie title and applies a score multiplier.

Point-Deducting Hint System: Users can type HINT during gameplay to reveal one hidden letter, resulting in a 5-point deduction from the current score.

Score and Streak Tracking: The game tracks the total score, rounds played, and maintains a counter for the player's longest consecutive correct guess streak.

Case-Insensitive Input: Guesses are normalized to ensure correct answers are accepted regardless of capitalization or minor spacing errors.
