#a python code that check for the prime number

#NumberToCheck = int(input("enter a number to check for prime: "))

def CheckForPrime(NumberToCheck):
    for x in range(2, NumberToCheck):
        if (NumberToCheck%x == 0):
            return False


    return True



CheckForPrime(10)