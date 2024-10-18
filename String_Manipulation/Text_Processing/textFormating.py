# Text Formatter: Create a program that allows users to format text with different styles, such as bold, italic, underline, and color. You can use ASCII escape sequences to achieve basic formatting.

def format_text(text,style='bold', color='white'):
    style_codes = {
      'bold': '\033[1m',
      'italic': '\033[3m',
      'underline': '\033[4m'
    }

    color_codes = {
      'white': '\033[37m',
      'red': '\033[31m',
      'green': '\033[32m',
      'blue': '\033[34m'
     }

    formated_text = style_codes[style] + color_codes[color] + text + '\033[0m'
    return formated_text

text = input("Enter Text: ")
text_style = input("Enter text style (bold, italic, underline): ")
color = input("Enter color ('red, green, blue): ")

print(format_text(text, text_style, color))
