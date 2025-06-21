 Password Guessing Game – Project Overview
This Python-based terminal game is a word guessing challenge where players try to unveil a secret word within a set number of attempts. The player selects from three difficulty levels—Easy, Medium, and Hard—each with progressively complex words and varying limits for attempts and hints.

The game provides:
-Real-time hint feedback using Wordle-style letter comparisons
-Hint system to reveal letters one by one (limited use)
-Time tracking to measure how long the player took
-Scoring system based on difficulty and number of attempts
-At the end of the game, players can see their score, time taken, and choose to replay.

🧠 Programming Language
-Python 3
Chosen for its simplicity, readability, and rich built-in libraries—perfect for scripting interactive terminal games.

🧰 Modules & Libraries Used
-random
Used to randomly select a secret word from the word list.
Also used to randomly reveal unrevealed letters during hints.

-time
Used to track gameplay duration, by capturing the start and end timestamps of a session.

💡 Concepts & Features Implemented
-Conditional logic and loops
-Functions for modular design
-Dynamic difficulty scaling
-User input validation
-List and string manipulation
-Hint logic similar to Wordle (with custom feedback: correct, present, or missing)
-Replay loop for continuous gaming fun
