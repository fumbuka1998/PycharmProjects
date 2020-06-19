#a program that allows user to enter two numbers and then swap them
x = int(input("enter first number: "))
y = int(input("enter second number: "))

print("------before swapping-------")
print("x is ",x)
print("y is ",y)

print("--------After swapping --------")

temp = x
x = y
y = temp

print("x is ",x)
print("y is ",y)

