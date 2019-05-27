import datetime
import enum

from flask_login import UserMixin
from sqlalchemy import (Column, DateTime, Enum, ForeignKey, Integer, Numeric,
                        String, Table, select)
from sqlalchemy.orm import relationship

from . import Base


class TransactionType(enum.Enum):
    """Enum."""

    INCOME = 0
    OUTGO = 1
    TRANSFER = 2


class PaymentType(enum.Enum):

    CASH = 0
    DEBIT = 1
    CREDIT = 2


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    _password = Column(String(128))

    def __init__(self, username, password):
        self.username = username
        self._password = password

    def __repr__(self):
        return f'User {self.username}'


account_transaction = Table('Account_Transaction', Base.metadata,
                            Column('account_id', Integer,
                                   ForeignKey('account.id')),
                            Column('transaction_id', Integer, ForeignKey('transaction.id')))


class Account(Base):
    """docstring for Account"""
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    bank = Column(String(50))
    description = Column(String(50), unique=True)
    balance = Column(Numeric(asdecimal=False))
    user_id = Column(Integer, ForeignKey('user.id'))
    creditcard_id = Column(Integer, ForeignKey(
        "creditcard.id"))
    transaction = relationship('Transaction',
                               secondary=account_transaction,
                               backref='account')

    def __init__(self, description, bank, balance, user, creditcard=None):
        self.description = description
        self.bank = bank
        self.balance = balance
        self.user_id = user.id
        if(creditcard):
            self.creditcard_id = creditcard.id


class Transaction(Base):
    """docstring for Transaction"""
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    value = Column(Numeric(asdecimal=False))
    date = Column(DateTime)
    payed_with = Column(Enum(PaymentType))
    parcels = Column(Integer, default=1)
    category_id = Column(Integer, ForeignKey('category.id'))
    transaction_type = Column(Enum(TransactionType))

    def __init__(self, description, value, date, payed_with, parcels, category, transaction_type):
        self.description = description
        self.value = value
        self.date = date
        self.payed_with = payed_with
        self.parcels = parcels
        self.category_id = category.id
        self.transaction_type = transaction_type


class Category(Base):
    """docstring for Categoria"""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)

    def __init__(self, description):
        self.description = description


class CreditCard(Base):
    __tablename__ = 'creditcard'
    id = Column(Integer, primary_key=True)
    limit = Column(Numeric(asdecimal=False))
    date_pay = Column(DateTime)

    def __init__(self, limit, account, date_pay):
        self.limit = limit
        self.account_id = account.id
        self.date_pay = date_pay
