#pip install emoji
from emoji import emojize as em
x=input("Input:")
y=em(x,language='alias')
#default language is 'en', but setting it to alias unlcoks the whole list of emojis
print("Output:",y)