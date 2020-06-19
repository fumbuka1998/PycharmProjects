#a pytho source code for the while loop tutorials

#code 1 for while loop in python
num = 1
sum = 0

while num != 0:
    num = float(input("enter number:"))
    sum = sum + num;

    print("the sum is ",sum)

else:
    print("the loop is over")

print("0------------------------------------0")

#code 2 for while loop in python
i = 1

while i<10:
    if i==5:
        continue
    print("the value of i is ",i)
    i+=1

print("the end of our loop")

print("0============================================0")