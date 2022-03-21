import spacy
from nltk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from spacy import displacy
from spacy import tokenizer

# nlp = spacy.load('en_core_web_sm')

def NERR(text):

    add=[]
    for sentence in text:
        
        add.append([ne_chunk(pos_tag(word_tokenize(sentence)))])
    return add

    
    