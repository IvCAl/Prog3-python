from lorem_text import lorem
def parrafos(n:int):
    text:str=""
    for i in range(n):
        text=text+lorem.words(10)+"\n"
    text=text[:-1]
    return text


print(parrafos(3))