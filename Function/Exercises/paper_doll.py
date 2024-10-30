# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text: str)->str:
    rslt = ''
    for char in text:
        rslt+= char*3
    return rslt

print(paper_doll("hello"))