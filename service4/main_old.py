import numpy as np
from fastapi import FastAPI
from service4.transactions import predictTransactions
from joblib import load

app = FastAPI()

model = load('random_forest_model.joblib')

@app.get('/')
def index():
    return{'Hello': 'Welcome to the Robs BANK'}

@app.post('/predict')
def predict(data: predictTransactions): 
    data_dict = data.dict() 
    features = np.array([list(data_dict.values())])
    #features = np.array([[data.TransactionID, data.TransactionAmt, data.ProductCD, data.card1, data.card2, data.card3, data.card4, data.card5, data.card6, data.addr1, data.addr2, data.P_emaildomain]])
    #model = load('random_forest_model.joblib')
    #model = _joblib.load("credit_card_xgboost.pkl")

    predictions = model.predict(features)
    if predictions == 1:
        result = "fraudulent"
    elif predictions == 0:
        result = "not fraudulent"

    return {'prediction': result}