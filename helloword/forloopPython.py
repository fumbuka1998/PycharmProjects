#python source code for the for loop tutorial

A = [0, 1, 2, 3, 4, 5] #list data type

B = (0, 1, 2, 3, 4, 5) #tuple data type

C = {0, 1, 2, 3, 4, 5} #set data type

D = '012345' #String data type

E = { #dictionary data type
    "name": "fumbuka",
    "age":22
    }

print(0 in A)

for i in C:
    if i==3:
        continue  
    print(i)
print("------------------------------------------")

for key, values in E.items():
    print(key, ' - ', values)
print("---------------------------------------")
    #range concept in python

for x in range(2, 30, 4):
    print(x)
else:
    print("the for loop loop is over")

print("0000---------------------------------------00000000")