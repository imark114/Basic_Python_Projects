# Word Frequency Counter: Count the occurrence of each word in a text file and display the results in descending order of frequency.

import collections
def count_word_frequency(filename):
    with open(filename,'r') as file:
        text = file.read()
    words = text.split()
    word_count = collections.Counter(words)
    return word_count

def display_word_frequency(word_count):
    for word, frequency in word_count.most_common():
        print(f"{word}: {frequency}")

filname = "test.txt"
display_word_frequency(count_word_frequency(filname))