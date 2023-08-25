from pydantic import BaseModel

class TransactionsVariables(BaseModel):
    TransactionID: int #como substituir o _id pelo transactionID mongodb
    TransactionAmt: float
    card1: int
    card2: int
    card5: int
    card6: int #crédito/ débito
    addr1: float
    P_emaildomain: float
    C1: float
    C2: float
    C4: float
    C8: float
    C13: float
    C14: float
    D1: float
    D2: float
    D3: float
    D4: float
    D10: float
    D15: float 
    M4: float
    V317: float 
    hour: int
    day: int
    dow: int