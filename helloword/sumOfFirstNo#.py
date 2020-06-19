#a python program to display the sum of all the first natural numbers suggested by the user

y = int(input("how many numbers to add:"))
sum = 0
for x in range(1, y+1):
    sum = sum + x

print("the sum of numbers is ", sum)