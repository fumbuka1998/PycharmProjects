#INDEX SLICING IN PYTHON

digits = [0,1,2,3,4,5,6,7,8,9]

print(digits[0])
print(digits[1])
print(digits[2])
print(digits[-2])
print(digits[-len(digits)])
print(digits[-10])
print(digits[2:6])

print(digits[::-2])
print()
print(digits[6:0:-2])

#it reverses a string
y = "fumbuka"
#print(y[::-1])
#print()

#making a tringle
for i in range(len(digits)):
    print(digits[0:i])
    print()


for i in range(len(y)):
    print(y[0:i])
    print()

#a better way to perform slicing using a variable window_size
#a dynamic slicing scheme
window_size = 7
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])











