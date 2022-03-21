from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, ne_chunk
from cgitb import text
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# nlp = spacy.load('en_core_web_sm')

def ALL(text):

    ps =PorterStemmer()
    x = WordNetLemmatizer()

    for sentence in text:

        add=[]
        res= [sub.split() for sub in text]
        s= " ".join([ps.stem(text) for text in sentence.split()])
        add.append(ps.stem(s))
        l= " ".join([x.lemmatize(text) for text in sentence.split()])
        add.append(l)
        add.append(pos_tag(word_tokenize(sentence)))
        add.append([ne_chunk(pos_tag(word_tokenize(sentence)))])
        add.append(res)
    return add
