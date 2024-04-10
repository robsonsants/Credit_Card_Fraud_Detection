import time
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import requests
import service1.orchestration as orchestration
import service1.variables as variables

#from service1.database import save_transaction

app = FastAPI()

def get_transaction_features(transaction_id: int) -> dict:
    print(f"Retrieving transaction features for ID: {transaction_id}")  # Debug print
    response = requests.get(f"http://18.229.138.53:8003/transaction/{transaction_id}")

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")

@app.post("/authorize_transaction")
def authorize_transaction(transaction: variables.TransactionsVariables):
        return {"message": "Transaction has been authorized.", "status_code": 200}

def save_to_file(times: dict):
    with open('execution_times.txt', 'a') as f:
        f.write(f"{times}\n")

@app.post("/transactions")
def receive_transaction(transaction: orchestration.Transaction):
    print(f"Received transaction: {transaction}")  # Debug print
    execution_times = {}
    # Retrieve additional data from the database
    start_time = time.time()
    additional_data = get_transaction_features(transaction.TransactionID)
    end_time = time.time()
    execution_times['retrieve_transaction_features'] = end_time - start_time
    #retrieve_transaction_features = end_time - start_time
    print(f"Time taken to receive transaction features: {end_time - start_time} seconds")

    # Remove keys that are already provided by the user
    for key in transaction.dict().keys():
        additional_data.pop(key, None)

    # Combine the user-provided data with the additional data
    full_data = {**transaction.dict(), **additional_data}
    #full_data = {**additional_data, **transaction.dict()}

    # Remove the '_id' and 'isFraud' keys
    #full_data.pop('_id', None)
    full_data.pop('isFraud', None)

    # Now full_data should have 223 features
    print(f"Full transaction data: {full_data}")  # Debug print

    # Call Service 4 for fraud detection
    fraud_detection_url = "http://15.229.87.129:8004/predict"
    start_time = time.time()
    response = requests.post(fraud_detection_url, json=full_data)
    end_time = time.time()
    execution_times['fraud_detection_service'] = end_time - start_time
    #fraud_detection_service = end_time - start_time
    print(f"Time taken to detect fraud: {execution_times} seconds")


    if response.status_code == 200:
        fraud_result = response.json().get("prediction")

        # Add debug print to see the result from the fraud detection service
        print(f"Fraud detection result: {fraud_result}")
        # Add the fraud detection result to the transaction data
         #full_data["isFraudulent"] = fraud_result

        # Save the transaction data to the database, regardless of the fraud detection result
        #save_transaction(full_data)

        if fraud_result == "fraudulent":
            # Transaction is fraudulent, stop the purchase
            print(f"Execution times: {execution_times}")
            save_to_file(execution_times)
            return {"message": "Transaction is fraudulent"}
        elif fraud_result == "not fraudulent":
            # Transaction is not fraudulent, continue with the purchase
            # Call Service 3 to authorize the transaction
            #service3_url = "http://db_service:8003/authorize_transaction"
            start_time = time.time()
            response = authorize_transaction(full_data)
            end_time = time.time()
            execution_times['authorize_transaction_service'] = end_time - start_time
            print(f"Time taken to authorize the transaction:: {execution_times} seconds")
            save_to_file(execution_times)

            if "status_code" in response and response["status_code"] == 200:
                # Add debug print to see the response from the transaction authorization service
                print(f"Transaction authorization response: {response}")
                return {"message": "Transaction successful"}
            else:
                # Add debug print to see the error from the transaction authorization service
                print(f"Transaction authorization error: {response}")
                raise HTTPException(status_code=500, detail="Failed to authorize transaction")



    else:
        # Add debug print to see the error from the fraud detection service
        print(f"Fraud detection service error: {response.text}")
        raise HTTPException(status_code=500, detail="Failed to call fraud detection service")