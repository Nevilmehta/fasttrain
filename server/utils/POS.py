from re import X
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import pos_tag
from nltk import RegexpParser

def POS(text):

    add=[]
    for sentence in text:
        add.append(pos_tag(word_tokenize(sentence)))
    return add
