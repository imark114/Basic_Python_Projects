# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(string: str)-> str:
    new_string = ''
    for i, letter in enumerate(string):
        if i == 0 or i == 3:
            new_string+= letter.upper()
        else:
            new_string+=letter

    return new_string

def old_macdonald2(name: str)->str:
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Too short name"

print(old_macdonald('macdonald'))
print(old_macdonald('bangladesh'))
print(old_macdonald2("maharishi"))