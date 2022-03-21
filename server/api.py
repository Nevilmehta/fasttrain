from audioop import add
from lib2to3.pgen2 import token
from pickle import FROZENSET
from turtle import pos
from fastapi import FastAPI
from server.models.model import request
from fastapi.encoders import jsonable_encoder
from server.utils.ALL import ALL
from server.utils.LEMMA import LEMMA
from server.utils.NERR import NERR
from server.utils.POS import POS
from server.utils.STEM import STEM
from server.utils.TOKEN import TOKEN

app= FastAPI()

@app.post("/fastapi/v1/LEMMA")
def do_LEMMA(item: request):
    
    payload= jsonable_encoder(item)
    lemmatization= LEMMA(payload.get("oper"))
    return ({"After lemmatization": lemmatization}) 

@app.post("/fastapi/v1/STEM")
def do_STEM(item: request):

    payload= jsonable_encoder(item)
    stemming= STEM(payload.get("oper"))

    return ({"After stemming": stemming}) 

@app.post("/fastapi/v1/POS")
def do_POS(item: request):

    payload= jsonable_encoder(item)
    pos= POS(payload.get("oper"))
    return ({"After pos": pos}) 

@app.post("/fastapi/v1/NERR")
def do_NERR(item: request):

    payload= jsonable_encoder(item)
    ner= NERR(payload.get("oper"))
    return ({"After ner": ner}) 

@app.post("/fastapi/v1/TOKEN")
def do_TOKEN(item: request):

    payload= jsonable_encoder(item)
    token= TOKEN(payload.get("oper"))
    return ({"After tokenization": token}) 

@app.post("/fastapi/v1/ALL")
def do_ALL(item: request):

    payload= jsonable_encoder(item)
    all= ALL(payload.get("oper"))
    lemmatization= LEMMA(payload.get("oper"))
    stemming= STEM(payload.get("oper"))
    pos= POS(payload.get("oper"))
    ner= NERR(payload.get("oper"))
    token= TOKEN(payload.get("oper"))
    return ({"stemming": stemming},{"lemmatization": lemmatization},{"pos": pos},{"ner": ner},{"tokenization": token}) 
