#sum of natural numbers
print("***Sum using loop***")
def sumNatural(limit):
    sum=0
    for x in range(1,limit+1):
        sum=x+sum
    print("The sum of natural numbers is from 1 till ",limit,"is = ",sum)
print("Calculate the sum of natural numbers")
limitVar=int(input("insert limit "))
sumNatural(limitVar)

#we can find th esum in multiple ways
#using formula and loops

print("***Sum using formula***")
Result=limitVar*(limitVar+1)/2
print("The sum of natural numbers is from 1 till ",limitVar,"is = ",Result)