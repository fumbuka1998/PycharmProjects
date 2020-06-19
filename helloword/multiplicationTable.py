#the mathematical table of any number entered by the user

n = int(input("enter your number to produce table: "))

for x in range(1, 13):
    print("\n", n, " x ", x, " = ",n*x)
