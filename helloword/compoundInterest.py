#the python code to find the compound interest

import math

p = int(input("enter the value of principle:"))
r = int(input("enter the value of rate:"))
t = int(input("enter the value of time period:"))

Ci = (p*pow((1 + r/100),t))

print("the compound interest obtained is ", Ci)