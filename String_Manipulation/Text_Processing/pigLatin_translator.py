# Pig Latin Translator: Implement a program that translates English words into Pig Latin. This involves moving the first letter to the end and adding "ay" (e.g., "hello" becomes "ellohay").

def pig_latin_translator_sentence(sentence):
    words = sentence.split()
    translated_words = [pig_latin_translator_word(word) for word in words]
    return ' '.join(translated_words)

def pig_latin_translator_word(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + 'ay'

sentence = input("Enter a Sentece: ")

print(f"In pig latin: {pig_latin_translator_sentence(sentence)}")



