#a python program to generate passwords

import random

s = "abcdefghijkl\
         mnopqrstuvwxyz1234\
          567890ABCDEFGHIJKLM\
          NOPQRSTUVWXYZ!@#$%^&*\
           ()_-+[]{};/':., "

passwordlen = 8

password = "".join(random.sample(s,passwordlen))
print(password)


