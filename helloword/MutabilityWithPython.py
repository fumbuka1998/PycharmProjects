
"""
                                      MUTABILITY WITH PYTHON
--->>>Explanning what mutability is in programming.
---->>>Examples of mutable and immutable devices
--->>>Explanation of how mutability allows us to have secure data

>mutability ----means changeble ie.list,dictionaries,orderedDict datatype since it can be changed.
......mutability for data flexibility.

>Immutability----means unchangeble  ie.tuple,ints,floats,booleans since it is stable and you can not add anything on it.
........immutability for secure data.

"""

t = (1,2,[1,2,3]) #a list which is a mutable within a tuple which is immutable
"""
--->>every thing in python is considered as an OBJECT, so the above tuple is considered as an object

--->>on the above tuple,t the location or pointer  of the list within the tuple 
     can not change but the values within the list can change
"""

print(t)
print()

t[2][0] = 54    #changing a  value within the list

print(t)

