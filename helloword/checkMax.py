#the python code to check for the value of the marks entered by the user
a = int(input("enter marks to be checked: "))

if a<=100 and a>=75:
    print("conguraturations you got A")

elif a<75 and a>=60:
    print("nice you have B")


elif a<60 and a>=50:
    print("average you got B-")


elif a<50 and a>=40:
    print("keep it up you got  C")


elif a<40 and a>=0:
    print("poor results you have F")

else:
    print("no such a marks my friend check again")
    a = int(input("enter marks to be checked: "))

