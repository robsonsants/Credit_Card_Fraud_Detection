import json
import time
import random
from fastapi import FastAPI, HTTPException, Request
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from variables import TransactionsVariables


#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#from service3.transaction import Transaction  # import your Transaction SQLAlchemy model here

app = FastAPI()

#client = MongoClient('mongodb://helpdev:123456@18.229.138.53:27017/')
#db = client['bank']
#collection = db['sample']

#collection.find_one({'TransactionID': 3054296})
#collection.find_one({"_id": ObjectId('646e54f8ac5e3481442020d7'),TransactionID: 3054296,})

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

transactions_dict = {}

def load_transactions():
        global transactions_dict
        with open('data_features_rf.json', 'r') as f:
                transactions = json.load(f)
        for transaction in transactions:
                transaction_id = transaction['TransactionID']
                transactions_dict[transaction_id] = transaction

load_transactions()
@app.get("/transaction/{transaction_id}")
def get_transaction(transaction_id: int):
        time.sleep(random.randint(120,150)/1000)
        transaction = transactions_dict.get(transaction_id)
        if transaction:
                return transaction
        else:
                raise HTTPException(status_code=404, detail="Transaction not found")

#@app.get("/transaction/{transaction_id}")
#def get_transaction(transaction_id: int):
#    transaction = collection.find_one({"TransactionID": transaction_id})
#    if transaction:
#       transaction['_id'] = str(transaction['_id'])
#       return transaction
#    else:
#       return {"error": "Transaction not found"}

#engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
#Session = sessionmaker(bind=engine)

@app.post("/authorize_transaction")
def authorize_transaction(transaction: TransactionsVariables):
    # Consider all transactions as authorized. You might want to add some logic here.
    return {"message": "Transaction has been authorized."}

#@app.get("/transaction_ids")
#def get_transaction_ids():
    # Busque todos os documentos e retorne apenas o campo TransactionID
#    transactions = collection.find({}, {"TransactionID": 1, "_id": 0})
    # Converta o cursor do MongoDB para uma lista e extraia os IDs de transação
#    transaction_ids = [transaction["TransactionID"] for transaction in transactions]

#    return transaction_ids
