"""
                 EMAIL ADDRESS AND TEXT  SCRAPER:
---->>>if i want to be able to search a bunch of text and pick up some emails from it we need a library in
       python called regular expression(re)



"""
import re

text = "fumbuka loves to program. limbu_fumbuka@gmail.com. my self and i we are enjoying python. limbumhozya@gmail.com"
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")


result = pattern.search(text)#it gives only one results
print(result)
print()
result = pattern.findall(text)#it check for all results

print(result)


























