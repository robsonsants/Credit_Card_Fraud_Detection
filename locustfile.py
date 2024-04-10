from locust import HttpUser, task, between
import random
import pandas as pd

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    teste = open("requisicao.csv", "r").readlines()

    def on_start(self):
        print("Running post_transaction...")
        

    @task
    def post_transaction(self):
        print("Running post_transaction...")
        #print(self.teste)

        r = random.randint(0,len(self.teste)-1)
        t = self.teste[r].split(',')
        print(f"About to post transaction: {self.teste[r]}")
        #print(t)
        transaction = {
            "TransactionID": int(t[0]),  # Use um ID de transação aleatório da lista
            "TransactionAmt": float(t[1]),
            "card1": int(t[2]),
            "card2": int(t[3]),
            "card5": int(t[4]),
            "card6": int(t[5]),
            "addr1": float(t[6]),
            "P_emaildomain": float(t[7])
        }
        #print(transaction)
<<<<<<< HEAD
        self.client.post("http://172.17.0.1:8001/transactions", json=transaction)
=======
        self.client.post("http://18.231.95.201:8001/transactions", json=transaction)
>>>>>>> 624a2976c9307c1459e6fb56acf28d8fc7ca2124
        #print(f"Response status: {response.status_code}, content: {response.text}")
        
        #print(f"About to post transaction: {transaction}")
        #response = self.client.post("http://localhost:8001/transactions", json=transaction)
        #print(f"Response status: {response.status_code}, content: {response.text}")
