import sys
import datetime

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


# we create the class USer and extend it from the Base Class.
# class Users(Base):
#     __tablename__ = 'Users'
#
#     id = Column(Integer, primary_key=True)
#     email = Column(String(250), nullable=False)
#     # surname = Column(String(250), nullable=False)
#     # date_of_birth = Column(String(250))
#     # account_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'Users'

    id = Column(String(500), primary_key=True)
    email = Column(String(250), primary_key=True)


class Accounts(Base):
    __tablename__ = 'Accounts'

    account_id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    balance = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)


class Transactions(Base):
    __tablename__ = 'Transactions'

    transaction_id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    account_mail = Column(String(250), nullable=False)
    receiver_bank_account = Column(Integer, nullable=False)
    transaction_description = Column(String(500), default="no description provided")
    date = Column(DateTime, default=datetime.datetime.utcnow)


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///payment_service.db')

Base.metadata.create_all(engine)
