import uvicorn
import numpy as np
from fastapi import FastAPI
from xgboost import DMatrix
import xgboost
from service4.transactions import predictTransactions
from joblib import load

app = FastAPI()

@app.get('/')
def index():
    return{'Hello': 'Welcome to the Robs BANK'}

@app.post('/predict')
def predict(data: predictTransactions): 
    data_dict = data.dict()
    features = np.array([list(data_dict.values())])
    #features_dmatrix = DMatrix(features)

    # Load the model
    #model_xgb = xgboost.Booster()
    #model_xgb.load_model("xgboost.bst")
    model = load("xgboost.bst")

    # Make predictions
    predictions = model.predict(features)
    if predictions == 1:
        result = "fraudulent"
    elif predictions == 0:
        result = "not fraudulent"

    return {'prediction': result}