import random
import time

easy_words = ["cat", "dog", "fish", "bird", "tree", "tiger", "lion", "shark", "india", "china","apple", "book", "car", "star", "moon", "milk", "rose", "frog", "duck", "leaf","cake", "rain", "snow", "shoe", "ball", "king", "queen", "ring", "ship"]

medium_words = ["elephant", "giraffe", "dolphin", "kangaroo", "penguin", "computer", "python", "javascript", "programming", "science", "history","mountain", "diamond", "holiday", "library", "sandwich", "umbrella", "hospital", "airplane", "calendar", "backpack","festival", "magazine", "language", "football", "building", "treasure", "painting", "triangle"]

hard_words = ["philosophy", "psychology", "mathematics", "astronomy", "architecture", "biochemistry", "neuroscience", "apprentice", "electromagnetism", "thermodynamics","microbiology", "cryptography", "paleontology", "metamorphosis", "photosynthesis", "circumference", "consciousness", "transcendence", "photosensitive", "infrastructure","multiculturalism", "counterintuitive", "uncharacteristic", "intercontinental", "misunderstanding", "reconciliation", "hypothetically", "unquestionable"]

def choose_word(level):
    if level in ("1", "easy"):
        return random.choice(easy_words)
    elif level in ("2", "medium"):
        return random.choice(medium_words)
    elif level in ("3", "hard"):
        return random.choice(hard_words)
    else:
        print("Invalid input. Defaulting to Easy level.")
        return random.choice(easy_words)

def get_hint(secret, guess):
    # Letter-by-letter feedback (like Wordle)
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += secret[i]
        elif i < len(guess) and guess[i] in secret:
            hint += "*"
        else:
            hint += "_"
    return hint

def reveal_letter(secret, revealed):
    unrevealed_indices = [i for i in range(len(secret)) if not revealed[i]]
    if not unrevealed_indices:
        return revealed
    idx = random.choice(unrevealed_indices)
    revealed[idx] = True
    return revealed

def display_word(secret, revealed):
    return ''.join([secret[i] if revealed[i] else '_' for i in range(len(secret))])

def get_max_hints(level):
    if level in ("1", "easy"):
        return 2
    elif level in ("2", "medium"):
        return 3
    elif level in ("3", "hard"):
        return 5
    else:
        return 2

def play_game():
    print("Welcome to the Password Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter the difficulty level: ").strip().lower()
    secret = choose_word(level)
    attempts = 0
    max_attempts = 8 if level in ("1", "easy") else 10 if level in ("2", "medium") else 12
    previous_guesses = []
    score = 0
    revealed = [False] * len(secret)
    hint_uses = 0
    max_hints = get_max_hints(level)

    print(f"\nStart guessing the word! It has {len(secret)} letters.")
    print(f"Type 'hint' to reveal a letter (can be used up to {max_hints} times).")
    print("Type 'quit' to exit the game early.")

    start_time = time.time()

    while attempts < max_attempts:
        print(f"\nWord: {display_word(secret, revealed)}")
        guess = input("Guess the word: ").strip().lower()
        if guess == "quit":
            print("You chose to quit the game.")
            break
        if guess == "hint":
            if hint_uses < max_hints:
                revealed = reveal_letter(secret, revealed)
                hint_uses += 1
                print(f"Hint used! Revealed letter: {display_word(secret, revealed)}")
                print(f"Hints left: {max_hints - hint_uses}")
            else:
                print("You have already used all your hints.")
            continue
        if not guess.isalpha():
            print("Please enter a valid alphabetic guess.")
            continue
        if len(guess) != len(secret):
            print(f"Please enter a word with {len(secret)} letters.")
            continue
        if guess in previous_guesses:
            print("You already guessed that word.")
            continue
        previous_guesses.append(guess)
        attempts += 1

        if guess == secret:
            score = (max_attempts - attempts + 1) * (10 if level in ("1", "easy") else 20 if level in ("2", "medium") else 30)
            print(f"\nCongratulations! You've guessed the word '{secret}' in {attempts} attempts.")
            break
        print(f"Hint: {get_hint(secret, guess)}")
        print(f"Attempts left: {max_attempts - attempts}")
        print(f"Previous guesses: {', '.join(previous_guesses)}")
    else:
        print(f"\nSorry, you've run out of attempts. The word was '{secret}'.")

    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    print(f"Time taken: {elapsed_time} seconds.")
    if score > 0:
        print(f"Your score: {score}")
    print("Game Over!")
    print("Thank you for playing the Password Guessing Game!")

    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay in ("yes", "y"):
        print("\nRestarting the game...\n")
        play_game()

if __name__ == "__main__":
    play_game()
