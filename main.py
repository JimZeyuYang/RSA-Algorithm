import random

def modulo(num, a):
    # Initialize result
    res = 0

    # One by one process all digits
    # of 'num'
    num = str(num)
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a;

    return res


dic = {"a": 1, "b": 2, "c": 3,
              "d": 4, "e": 5, "f": 6,
              "g": 7, "h": 8, "i": 9,
              "j": 10, "k": 11, "l": 12,
              "m": 13, "n": 14, "o": 15,
              "p": 16, "q": 17, "r": 18,
              "s": 19, "t": 20, "u": 21,
              "v": 22, "w": 23, "x": 24,
              "y": 25, "z": 26, " ": 27,
              ",": 28, ".": 29, ";": 30,
              ":": 31, "?": 32, "!": 33
              }

# Task1
while True:
    isPrime = True
    p = random.randint(2,100)

    for i in range(2, p):
        if p % i == 0:
            isPrime = False
    if isPrime:
        print(p)
        break

while True:
    isPrime = True
    q = random.randint(2, 100)

    for i in range(2, q):
        if q % i == 0:
            isPrime = False
    if isPrime:
        print(q)
        break
n=p*q
print(n)

def totient(q, p):
    return (q-1)*(p-1)


totient=totient(q,p)
print(totient)


while True:
    Coprime=True
    public= random.randint(2,totient)
    for i in range(2,totient):
        if totient %i==0:
            if public%i==0:
                Coprime=False
    if Coprime:
        print(Coprime)
        print(public)
        break

while True:
    private=random.randint(2,10000)
    if modulo((private*public),n) == 1:
        print(private)
        break

# Task2
def getKeys(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys


def encrypt(input,n,public):
    input=input.lower()
    encrypted=list()
    for i in range(0,len(input)):
        encrypted.append(modulo(dictionary[input[i]]**public,n))
    return encrypted


print(encrypt("I am amazed by how easy it is programming!", 923, 713))


def decrypted(input,n,private):
    output=list()
    for i in range(0,len(input)):
        output += getKeys(dictionary,modulo(input[i]**private,n))

    return ''.join(output)

testdata = [602, 551, 129, 129, 365, 374, 617, 898, 551, 308, 308, 308, 898, 617, 602, 365,
      857, 617, 788, 365, 373, 1, 898, 365, 551, 1, 171, 679, 129, 857, 365, 551, 898,
     373, 617, 374, 551, 365, 602, 229, 1, 245, 551, 68, 551, 512, 365, 374, 1, 245, 1,
      365, 857, 617, 788, 365, 602, 1, 898, 245, 921]

print(decrypted(testdata, 923, 377))
