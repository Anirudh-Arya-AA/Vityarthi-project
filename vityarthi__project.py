# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 14:41:18 2025

@author: CHEETAH
"""

import random
import time

class MovieGuessingGame:
    def __init__(self):
        self.movies = []
        self.placeholder = "*"
        self.score = 0
        self.total_rounds = 0
        self.correct_guesses = 0
        self.streak = 0
        self.max_streak = 0
        self.difficulty = "MEDIUM"
        self.difficulty_multiplier = 1.0

    def clear_screen(self):
        print("\n" * 50)

    def print_banner(self):
        print("=" * 50)
        print("||                                              ||")
        print("||           ULTIMATE MOVIE GUESSER             ||")
        print("||                                              ||")
        print("=" * 50)

    def get_difficulty_setting(self):
        print("\nSelect Difficulty:")
        print("1. Easy   (10% hidden, x1.0 score)")
        print("2. Medium (30% hidden, x1.5 score)")
        print("3. Hard   (50% hidden, x2.0 score)")
        
        while True:
            choice = input("Choose (1-3): ").strip()
            if choice == "1":
                self.difficulty = "EASY"
                self.difficulty_multiplier = 1.0
                return 0.10
            elif choice == "2":
                self.difficulty = "MEDIUM"
                self.difficulty_multiplier = 1.5
                return 0.30
            elif choice == "3":
                self.difficulty = "HARD"
                self.difficulty_multiplier = 2.0
                return 0.50
            print("Invalid selection. Try again.")

    def setup_game(self):
        self.print_banner()
        print("\n[ SYSTEM SETUP ]")
        
        while True:
            print("\nEnter movie titles (separated by commas).")
            print("Example: Matrix, Star Wars, Titanic")
            user_input = input("Movies: ")
            cleaned_list = [m.strip() for m in user_input.split(',') if m.strip()]
            
            if len(cleaned_list) >= 1:
                self.movies = cleaned_list
                break
            print("Error: You must enter at least one valid movie title.")

        p_char = input("Enter placeholder character (default '*'): ").strip()
        if len(p_char) > 0:
            self.placeholder = p_char[0]
        else:
            self.placeholder = "*"
            
        print("\nSetup Complete. Initializing Game...")
        time.sleep(1)

    def obfuscate_title(self, title, percentage):
        chars = list(title)
        alpha_indices = [i for i, c in enumerate(chars) if c.isalpha()]
        
        if not alpha_indices:
            return title
            
        count_to_hide = max(1, int(len(alpha_indices) * percentage))
        indices_to_hide = random.sample(alpha_indices, count_to_hide)
        
        for i in indices_to_hide:
            chars[i] = self.placeholder
            
        return "".join(chars)

    def reveal_hint(self, current_mystery, original_title):
        chars_mystery = list(current_mystery)
        chars_original = list(original_title)
        hidden_indices = [i for i, c in enumerate(chars_mystery) if c == self.placeholder]
        
        if not hidden_indices:
            return current_mystery
            
        reveal_index = random.choice(hidden_indices)
        chars_mystery[reveal_index] = chars_original[reveal_index]
        
        return "".join(chars_mystery)

    def show_stats(self):
        print("\n" + "-" * 30)
        print("       GAME STATISTICS       ")
        print("-" * 30)
        print(f"Total Score:    {int(self.score)}")
        print(f"Rounds Played:  {self.total_rounds}")
        print(f"Accuracy:       {self.correct_guesses}/{self.total_rounds}")
        print(f"Best Streak:    {self.max_streak}")
        print("-" * 30)

    def play_round(self, hide_percentage):
        self.total_rounds += 1
        target_movie = random.choice(self.movies)
        mystery_string = self.obfuscate_title(target_movie, hide_percentage)
        attempts = 0
        max_attempts = 3
        round_active = True
        
        print(f"\n>>> ROUND {self.total_rounds} <<<")
        
        while round_active:
            print(f"\nMystery: {mystery_string}")
            print(f"Attempts remaining: {max_attempts - attempts}")
            print("(Type 'HINT' for a letter [-5 pts] or 'QUIT' to exit)")
            
            guess = input("Your Guess: ").strip()
            
            if guess.upper() == "QUIT":
                return False
                
            if guess.upper() == "HINT":
                if self.score >= 5:
                    self.score -= 5
                    mystery_string = self.reveal_hint(mystery_string, target_movie)
                    print("Hint used! 5 points deducted.")
                else:
                    print("Not enough points for a hint!")
                continue

            if guess.lower() == target_movie.lower():
                base_points = 100
                bonus = (max_attempts - attempts) * 20
                total_round_points = (base_points + bonus) * self.difficulty_multiplier
                
                self.score += total_round_points
                self.correct_guesses += 1
                self.streak += 1
                if self.streak > self.max_streak:
                    self.max_streak = self.streak
                    
                print(f"\nCORRECT! The movie was: {target_movie}")
                print(f"Points earned: {int(total_round_points)}")
                print(f"Current Streak: {self.streak}")
                round_active = False
                
            else:
                attempts += 1
                print("Incorrect guess.")
                self.streak = 0
                
                if attempts >= max_attempts:
                    print(f"\nGAME OVER for this round.")
                    print(f"The correct answer was: {target_movie}")
                    round_active = False

        return True

    def start(self):
        self.setup_game()
        hide_percent = self.get_difficulty_setting()
        
        game_running = True
        while game_running:
            continue_game = self.play_round(hide_percent)
            if not continue_game:
                break
                
            valid_response = False
            while not valid_response:
                again = input("\nPlay another round? (y/n): ").lower().strip()
                if again == 'y':
                    valid_response = True
                elif again == 'n':
                    valid_response = True
                    game_running = False
                else:
                    print("Please enter 'y' or 'n'")
        
        self.show_stats()
        print("\nThanks for playing!")

if __name__ == "__main__":
    game = MovieGuessingGame()
    game.start()