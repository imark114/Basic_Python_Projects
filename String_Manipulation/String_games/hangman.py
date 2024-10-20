# Hangman Game: Implement the classic word guessing game, where the player tries to guess a hidden word by suggesting letters.

import random

def display_game(game_state):
    word = game_state['word']
    guessed_letters = game_state['guessed_letters']

    display_word = ''.join('_' if letter not in guessed_letters else letter for letter in word)
    print(display_word)
    print(f"Guessed letters: {', '.join(guessed_letters)}")

def play_hangman(word_list):
    word = random.choice(word_list)
    game_state = {'word': word, 'guessed_letters': set(), 'attempts': 6}

    while game_state['attempts'] > 0:
        display_game(game_state)
        guess = input("Guess a letter: " ).lower()
        if guess in game_state['guessed_letters']:
            print("You already guessed that letter.")
        elif guess in word:
            game_state['guessed_letters'].add(guess)
        else:
            game_state['attempts']-=1
            print(f"Incorrect guess. You have {game_state['attempts']} attempts left")
        if '_' not in ''.join([letter if letter in game_state['guessed_letters'] else '_' for letter in word]):
            print("Congratulations! You won. The Wrod is", word)
            return
    print("Game over. The word was:", word)

word_list = ["hello", "world", "python", "programming"]
play_hangman(word_list)