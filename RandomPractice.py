import random

#define a function to randomly generate a given length string
def generateOne(n):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    return random.choices(alphabet,k=n)
#the first method returns a list of letters

def generateTwo(n):
    alphabet="abcdefghijklmnopqrstuvwxya "
    teststring=""
    for i in range(n):
        teststring=teststring+alphabet[random.randrange(len(alphabet))]
    return teststring
#the second method returns a string

#define a function to score a generated string, by comparing the goalstring and teststring
def score(goalstring,teststring):
    samesum=0
    for i in range(len(goalstring)):
        if goalstring[i]==teststring[i]:
            samesum+=1
    score = samesum/len(goalstring)
    return score

#using while loop to find out the string with highest score for the first 1million generations.
def beststring(goalstring,trytimes):
    bestscore=0
    i=0
    while i<trytimes:
        teststring=generateOne(len(goalstring))

        if score(goalstring,teststring)>bestscore:
            bestscore=score(goalstring,teststring)
            beststring=teststring
        i+=1
    return (bestscore,beststring)

print(beststring('abcd',10000))
print(beststring('abcd',1000000))