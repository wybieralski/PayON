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
class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    date_of_birth = Column(String(250))
    account_id = Column(Integer, nullable=False)


class Accounts(Base):
    __tablename__ = 'Accounts'

    id_account = Column(Integer, primary_key=True)
    balance = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)


class Transactions(Base):
    __tablename__ = 'Transactions'

    transaction_id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    seller_id = Column(Integer, nullable=False)
    buyer_id = Column(Integer, nullable=False)


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///payment_service.db')

Base.metadata.create_all(engine)
