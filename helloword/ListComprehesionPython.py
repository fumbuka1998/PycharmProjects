"""
         LIST COMPREHESIONS IN PYTHON


"""

names = ['fumbuka','mlasa','selesi','mudy']

l = []
for person in names:
    l.append(person)

#print(l)
#print()
#print([person for person in names])#comprehesion
#print()

#list operations

l = []
for person in names:
    l.append(person + ' limbu')
print(l)
print([person + ' limbu' for person in names])#comprehesion
print()
print()

movies_and_rating = {'merlin':9,'black parther':6,'johari':3,'family tears':4}

l = []
for movies in movies_and_rating:
    if movies_and_rating[movies]>5:
        l.append(movies)

print(l)

print([movies for movies in movies_and_rating if movies_and_rating[movies]>6])



