# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_craker(string: str)-> bool:
    words = string.split()
    return True if words[0][0] == words[1][0] else False

print(animal_craker('Levelheaded Llama'))
print(animal_craker('Crazy Kangaroo'))