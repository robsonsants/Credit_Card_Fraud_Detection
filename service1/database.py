from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from service1.transaction import Transaction  # import the Transaction class from your models.py file

engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')  # Global engine
Session = sessionmaker(bind=engine)  # Global Session class

def save_transaction(transaction_data):
    # Create a SQLAlchemy Session
    session = Session()

    # Create a Transaction object from the transaction data
    transaction = Transaction(**transaction_data)

    # Add the transaction to the session and commit
    session.add(transaction)
    session.commit()

    # Close the session
    session.close()