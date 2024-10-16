# Determine if a given word or phrase is a palindrome (reads the same backward as forward).

def is_palindrom(words):
    word = words.replace(' ','').replace(',', '').replace('.','').lower()
    return word == word[::-1]

word = input("Enter a phrase or word: ")
if is_palindrom(word):
    print("The word is palindrom!")
else:
    print("The word is not palindrom")