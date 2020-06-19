#LIST DATATYPE IN PYTHON
#---it means the collections of things in order
#[1, 2, 3, 4, 5] an example of a list datatype
#[] ----is an empty list

l = [2, 3, 4, 5, 7,8]

l2 = [34, "fumbuka", "python", 4.6, 5.0, [34,78,97,54,]]

print(l)
print(l2)
print(l2[0])
print(l2[2])
print(l2[4])
print(l2[1])
print(l2[5])
print(l2[3])

print()
print()
print()

#adding an element to the end of the list using the append()

names = ["fumbuka", "muddy", "rehema"]

print(names)
print()

names.append("mlasa")
names.insert(0,"python")
print(names)
print()

names.remove("muddy")
names.reverse()
print(names)
print()
print()

#sorting numbers

numbers = [4, 5,1,0,7,9]

print("before sorting")
print(numbers)
print()

print("After sorting the numbers ascending order")
numbers.sort()
print(numbers)
print()

#iterations in for loop

for i in numbers:
    print(i)