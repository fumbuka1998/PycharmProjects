#SETS IN PYTHON
#sets is just like the tuples or list except the elements in sets are enclosed within {}
#this is another way of grouping things or elements in python
#it does not allow duplication of elements in a set {}

s = {'fumbuka','mlasa'}
s.add('mhozya')
s.add(5)
#print(s)



l = [1,2,2,2,2,2,3,4,5,6,6,6,6,7,8]

no_duplicate_set = set(l)

#print(no_duplicate_set)

#sets operations ie.union,intersection etc

library_1 = {'city hunter','a man called GOD','Merlin'}
library_2 = {'city hunter','Mr Robot'}

all_books = library_1.union(library_2)
print(all_books)

books = library_1.intersection(library_2)
print(books)


difffers = library_1.difference(library_2)
print(difffers)

differs2 = library_2.difference(library_1)
print(differs2)


