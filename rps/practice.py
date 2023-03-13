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
random_arithmetic(5, 10)