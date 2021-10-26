import time
userNum = int(input("What number would you like to start with? "))

def checkEvenOrOdd(numb):
    if (numb % 2) == 0:  
        newNum = numb / 2
        print(newNum)
        return newNum
    if (numb % 2) != 0:
        newNum = numb * 3 + 1
        print(newNum)
        return newNum

checkEvenOrOdd(userNum)
while True:
    checkEvenOrOdd(newNum)