#A PYTHON FUNCTION TO REVERSE A STRING

def Reverse_String(x):
    return x[::-1]
myString = input("Enter any text to reverse: \n")
print()
print("this is the reversed text:")

myText = Reverse_String(myString)
print(myText)