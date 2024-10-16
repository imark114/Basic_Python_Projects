# Text Analyzer: Create a tool that can count words, characters, sentences, and paragraphs in a given text. It can also provide basic text statistics like average word length.
import re

def analyze_text(text):
    character_count = len(text)
    word_count = len(re.findall(r'\b\w+\b', text))
    sentence_count = len(re.findall(r'[.?!]', text))
    paragraph_count = len(re.findall(r'\n\n+',text))
    avarage_word_lenght = character_count / word_count if word_count > 0 else 0

    return{
        'Character Count': character_count,
        'Word Count': word_count,
        'Sentece Count': sentence_count,
        'Paragraph Count': paragraph_count,
        'Avarage Word Length': avarage_word_lenght
    }

text = input("Enter a text: ")
result = analyze_text(text)
print(result)