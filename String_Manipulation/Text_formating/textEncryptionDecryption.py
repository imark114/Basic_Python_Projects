# Text Encryption/Decryption: Implement a simple encryption algorithm using substitution or transposition techniques. While not suitable for highly secure applications, it's a good exercise in string manipulation.
def caser_cipher_encrypttion(text, shift):
    alphates = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char.isalpha():
            index = (alphates.index(char) + shift) % 26
            encrypted_text+=alphates[index]
        else:
            encrypted_text+=char
    return encrypted_text

def case_cipher_decryption(text, shit):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text= ''
    
    for char in text.lower():
        if char.isalpha():
            index = (alphabets.index(char) - shit + 26) % 26
            decrypted_text+=alphabets[index]
        else:
            decrypted_text+=char
    return decrypted_text

text = input("Enter text: ")
print(caser_cipher_encrypttion(text,3))
d_text = input("Enter Encrypted Text: ")
print(case_cipher_decryption(d_text,3))