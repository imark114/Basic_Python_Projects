# Anagram Solver: Given a word, find all possible anagrams of that word from a dictionary.

from collections import Counter

def find_anagram(word, dictionary):
    word_count = Counter(word)
    anagrams = []

    for dic_word in dictionary:
        if Counter(dic_word) == word_count:
            anagrams.append(dic_word)
    return anagrams

word = "tea"
dictionary = ["eat", "tea", "ate", "bat", "lat"]
print(find_anagram(word, dictionary))
