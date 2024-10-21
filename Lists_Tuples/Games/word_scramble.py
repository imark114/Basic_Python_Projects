# Word Scramble: Create a word scramble game by generating a list of scrambled words. Allow the user to unscramble the words and keep track of their score.
import random

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)
def play_word_scramble():
    words = ["apple", "banana", "orange", "grape", "pear", "strawberry", "blueberry", "raspberry"]
    scrable_words = [scramble_word(word) for word in words]
    score = 0

    for i,scrable_word in enumerate(scrable_words):
        print(f"Scramble word {i+1}: {scrable_word}")
        user_answer = input("Enter your answer: ")
        if user_answer.lower() == words[i]:
            print("Correct!")
            score+=1
        else:
            print(f"Incorrect. The answer is {words[i]}")
    print(f"Your final score is: {score} out of {len(words)}")

play_word_scramble()