import nltk
from nltk.tokenize import word_tokenize

def TOKEN(text):

    add=[]
    res= [sub.split() for sub in text]
    add.append(res)
    return add