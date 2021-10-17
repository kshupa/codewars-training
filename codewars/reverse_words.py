'''Complete the function that accepts a string parameter, 
and reverses each word in the string. 
All spaces in the string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

import re


def reverse_words(text):
    pass


text = 'hello  my!'
words = re.finditer(r'\S+', text)
print(words)
for word in words:
    print(word)
