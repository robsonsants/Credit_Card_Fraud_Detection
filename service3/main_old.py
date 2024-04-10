import json

from fastapi import FastAPI, HTTPException, Request
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from service3.variables import TransactionsVariables
from service3.variables import ClientTransactionInfo

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#from service3.transaction import Transaction  # import your Transaction SQLAlchemy model here

app = FastAPI()

#client = MongoClient('mongodb://helpdev:123456@mongodb:27017/')
#client = MongoClient('mongodb://helpdev:123456@ec2-15-228-59-188.sa-east-1.compute.amazonaws.com:27017/')
#db = client['bank']
#collection = db['sample']

#collection.find_one({'TransactionID': 3054296})
#collection.find_one({"_id": ObjectId('646e54f8ac5e3481442020d7'),TransactionID: 3054296,})

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
    
transactions_dict = {}  # Dicionário para armazenar todas as transações

def load_transactions():
    global transactions_dict
    with open('data_features_rf.json', 'r') as f:
        transactions = json.load(f)
    for transaction in transactions:
        transaction_id = transaction['TransactionID']
        transactions_dict[transaction_id] = transaction  # Armazenar transação no dicionário

load_transactions()  # Carregar todas as transações quando a aplicação iniciar

@app.get("/transaction/{transaction_id}")
def get_transaction(transaction_id: int):
    transaction = transactions_dict.get(transaction_id)

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return transaction


#@app.get("/transaction/")
#def get_transaction(client_info: ClientTransactionInfo):
#    transaction_id = client_info.TransactionID
#    transaction = transactions_dict.get(transaction_id)

#    if transaction is None:
#        return {"error": "Transaction not found"}

    # Combine the client's transaction info with the rest of the info
#    full_transaction_info = {**transaction, **client_info.dict()}

#    return full_transaction_info

#engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
#Session = sessionmaker(bind=engine)

@app.post("/authorize_transaction")
def authorize_transaction(transaction: TransactionsVariables):
    # Consider all transactions as authorized. You might want to add some logic here.
    return {"message": "Transaction has been authorized."}

@app.get("/transaction_ids")
def get_transaction_ids():
    # Pegar todos os IDs de transação do dicionário
    transaction_ids = list(transactions_dict.keys())
    return transaction_ids