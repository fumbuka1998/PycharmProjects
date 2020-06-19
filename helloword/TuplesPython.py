#TUPLES IN PYTHON DATATYPES
#---it is used for the security of the data
# --you can not add or remove element in tuple
#-------is a kind of stable,structured datatype

t = (2,3,45,6,8) #declaring a tuple
print(t)
print()

credit_card1 = (2328973958742,'fumbuka','NMB mikocheni',498)
credit_card2 = (2328973958742,'fumbuka','NMB mikocheni',498)

credit_cards = [credit_card1,credit_card2]

#print(credit_cards)

#a person tuples

person1 = ('fumbuka', 22, 'karate')
person2 = ('mlasa', 20, 'football')

people  = [person1, person2]

for Name,age,favSport in people:
    print('Name: ',Name)
    print('Age: ',age)
    print('Favourate sport: ',favSport)
    print()
    print()

