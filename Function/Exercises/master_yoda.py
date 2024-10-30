# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentece:str) -> str:
    words = sentece.split()
    return ' '.join(words[::-1])

print(master_yoda("I am home"))
print(master_yoda("We are ready"))