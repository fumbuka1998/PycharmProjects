#DICTIONARIES IN PYTHON
#they are real good for:
#-----super organized data(mini databases)
#=----fast as hell(constant time)
#
#
#QN1:How to create dictionaries
#QN2:How to index into dictionaries
#QN3:How to add to dictionaries
#QN4:What"key-value pairs" are in an element of a dictionary
#        METHODS IN DICTIONARY DATATYPES
#get()   items()   keys()  values()  pop()  popitem()
#clear()
#
#
#
from collections import OrderedDict
movies = {'merlin':5, 'social network':9, 'jobs':8}

#print(movies['jobs'])
#print(movies.get('merlin'))
#print(movies.get('fumbu'))

contacts = {
    'fumbuka':{'phone':'0765-334612','email':'limbufumbuka@gmail.com'},#a dictionary within a dictionary
    'mlasa':['0765-222999','limbumhozya@gmail.com'] #a list within a dictionary
}

#print(contacts['fumbuka'])

#dict.items()
print(list(movies.items()))

#dict.keys()
print(list(movies.keys()))

#dict.value()
print(list(movies.values()))

print()
print()

#a method to remove  element from a dictionary   ie. dict.pop(key)
print(movies)
movies['Bad land'] = 23 #adding an item into a dictionary
movies.pop('jobs')

print(movies)
print()
movies.popitem()
print(movies)
print()

#dict.clear()----a method to empty the dictionary
movies.clear()
#print(movies)

