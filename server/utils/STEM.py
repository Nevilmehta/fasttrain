from cgitb import text
from nltk.stem import PorterStemmer

def STEM(text):

    ps =PorterStemmer()
    add=[]
    for sentence in text:
        s= " ".join([ps.stem(text) for text in sentence.split()])
        add.append(s)
        #return " ".join([ps.stem(text) for text in sentence.split()])
    return add
