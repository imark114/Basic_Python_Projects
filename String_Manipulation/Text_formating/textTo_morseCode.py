# Text to Morse Code Converter: Convert text into Morse code and vice versa. Use dictionaries to map characters to their corresponding Morse code representations.

morse_codes = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.','q': '--.-',
    'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' '
}

def text_to_morse(text):
    morese_code_text = ""

    for char in text.lower():
        if char in morse_codes:
            morese_code_text+= morse_codes[char] + " "
    return morese_code_text

def morse_to_text(morse_code):
    text = ""
    morse_code_words = morse_code.split()

    for word in morse_code_words:
        for char in word:
            for key, value in morse_codes.items():
                if value == char:
                    text+=key
        text+=' '
    return text.strip()

text = "hello world"
morse_code = text_to_morse(text)
print(morse_code)
print(morse_to_text(morse_code))