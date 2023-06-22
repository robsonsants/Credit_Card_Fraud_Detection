from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import pandas as pd
import json
import os


import service3.variables as variables

from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}
# Conectar ao MongoDB
#client = MongoClient('mongodb://mongodb:27017/bank')
#db = client['mongo']
# Conectar ao MongoDB
client = MongoClient('mongodb://mongodb:27017/')
# Conectar ao MongoDB
#client = MongoClient(f"mongodb://{os.environ['MONGODB_HOST']}:27017/")
db = client['bank']
collection = db['transactions']

# Ler o arquivo JSON
with open('data.json', 'r') as f:
   data = json.load(f)

# Atribuir o TransactionID como o _id do MongoDB
for document in data:
    document['_id'] = document['TransactionID']

collection.insert_many(data)

@app.get("/transaction/{transaction_id}", response_model=variables.TransactionsVariables)
async def get_transaction(transaction_id: int) -> Optional[variables.TransactionsVariables]:
    # Obter a transação do MongoDB
    transaction = db.transactions.find_one({"_id": transaction_id})

    # Se a transação não for encontrada, retorna None
    if transaction is None:
        return None

    # Remove o _id porque não está na classe TransactionsVariables
    transaction.pop('_id', None)

    return transaction