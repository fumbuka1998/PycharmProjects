#a print statement to display  different sentences
print("fumbuka is enjoying python programming")
print("wewe ni programmer!")

i=0

#while loop in python programming
#while(i<5):
   # print("mimi ni programmer najikubali")
    #i += 1


#a for loop in python lang

fruits = ["mango","ubuyu","ndizi"]
for x in fruits:
    if x=="ubuyu":
        continue
   # print(x)

""" this is another way of writing a
 comment
 
 this is a multi- line comments """

#range function
#for x in range(10):
   #print("sisi ndo wanyabi")

#recursive function
import math
def tri_recursion(k):
    if(k>0):
        result =k + tri_recursion(k-1)
        print(result)

    else:
        result = 0
        return result

    print("\n\n Recursion results are:")

    print(tri_recursion(5))

