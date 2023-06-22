from typing import Optional
from fastapi import FastAPI 
from pydantic import BaseModel

class Transaction(BaseModel):
    TransactionID: int
    TransactionAmt: Optional[float] = None
    card1: Optional[int] = None
    card2: Optional[int] = None
    card5: Optional[int] = None
    card6: Optional[int] = None
    addr1: Optional[float] = None
    P_emaildomain: Optional[float] = None

