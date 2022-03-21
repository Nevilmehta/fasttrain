from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
	
def LEMMA(text):

    x = WordNetLemmatizer()
    add=[]
    for sentence in text:
        l= " ".join([x.lemmatize(text) for text in sentence.split()])
        add.append(l)
    return add
        #return " ".join([x.lemmatize(text) for text in sentence.split()])