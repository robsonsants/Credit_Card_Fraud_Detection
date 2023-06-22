from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    TransactionID = Column(Integer, primary_key=True)
    TransactionAmt = Column(Float)
    card1 = Column(Integer)
    card2 = Column(Integer)
    card5 = Column(Integer)
    card6 = Column(Integer)
    addr1 = Column(Float)
    P_emaildomain = Column(Float)
    C1 = Column(Float)
    C2 = Column(Float)
    C4 = Column(Float)
    C8 = Column(Float)
    C13 = Column(Float)
    C14 = Column(Float)
    D1 = Column(Float)
    D2 = Column(Float)
    D3 = Column(Float)
    D4 = Column(Float)
    D10 = Column(Float)
    D15 = Column(Float)
    M4 = Column(Integer)
    V317 = Column(Float)
    hour = Column(Integer)
    day = Column(Integer)
    dow = Column(Integer)
    isFraudulent = Column(String)
    # You may have more columns here depending on your data