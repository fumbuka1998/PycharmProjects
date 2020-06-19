#SPLITTING AND JOINNING STRING

students = 'fumbuka, juma, sambeke, mlasa'
print(students)

print()

l = students.split(", ")

#print(l)

#l = students.split("juma")
#print(l)

#joining

joined = ' and '.join(l)
print(joined)

csv = ','.join(l)
print(csv)
