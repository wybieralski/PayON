from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Base, Accounts, Transactions
from datetime import datetime
from random import randrange


# bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///payment_service.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

# Create
time = datetime.now()
print(time)

user1 = User(id=str(567), email="some@email.com")
user2 = User(id=str(1054635430), email="some2@email.com")
user3 = User(id=str(105465989180335430), email="some3@email.com")

account1 = Accounts(email="some@email.com", balance = 0, created_date=time)
account2 = Accounts(email="some2@email.com",  balance = 0, created_date=time)
account3 = Accounts(email="some3@email.com", balance = 0)

transaction1 = Transactions(account_mail="some3@email.com",receiver_bank_account=2, transaction_description="Cinema tickets",amount=20)
transaction2 = Transactions(account_mail="some3@email.com",receiver_bank_account=1, transaction_description="Sport activities",amount=20)
transaction3 = Transactions(account_mail="some3@email.com",receiver_bank_account=1,amount=20)



session.add(transaction1)
session.add(transaction2)
session.add(transaction3)
session.add(account3)
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()
session.close()
