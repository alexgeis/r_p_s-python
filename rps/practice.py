from random import randint

def random_letters():
    randLetter1 = chr(randint(97,122))
    randLetter2 = chr(randint(97,122))
    return print((randLetter1, randLetter2))

# random_letters()

def random_arithmetic(int1: int, int2: int) -> str:
    opList = ["+","-","*","/"]
    randomIndex = randint(0,3)

    evalStr = str(int1) + " " + opList[randomIndex] + " " + str(int2)
    evalValue = eval(evalStr)
    return print(evalStr + " = " + str(evalValue))
# random_arithmetic(5, 10)

def is_vowel(letter:str) -> str:
    unicodeVal = ord(letter.lower())
    if (unicodeVal == 97 or
        unicodeVal == 101 or
        unicodeVal == 105 or
        unicodeVal == 111 or
        unicodeVal == 117):
        return print(True)
    else: 
        return print(False)
is_vowel("a")
is_vowel("f")
is_vowel("o")
is_vowel("y")