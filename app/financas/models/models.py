import enum
import os

from sqlalchemy import (Column, DateTime, Enum, ForeignKey, Integer, Numeric,
                        String, Table, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class TransactionType(enum.Enum):
    """Enum."""

    INCOME = 0
    OUTGO = 1
    TRANSFER = 2


''' class MySession():

    def __init__(self, base, test=False):
        """Inicializa."""
        if test:
            path = ':memory:'
        else:
            path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'sqlite.db')
        self._engine = create_engine('sqlite:///' + path, convert_unicode=True)
        Session = sessionmaker(bind=self._engine)
        if test:
            self._session = Session()
        else:
            self._session = scoped_session(Session)
            base.metadate.bind = self._engine

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine

 '''
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'


class Account(Base):
    """docstring for Conta"""
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)
    balance = Column(Numeric(asdecimal=False))
    credit_card_id = Column(Integer, ForeignKey(
        "creditcard.id"))

    def __init__(self, description):
        self.description = description


class Transaction(Base):
    """docstring for Transacao"""
    __tablename__ = 'transacao'
    id = Column(Integer, primary_key=True)
    outgo_id = Column(Integer, ForeignKey('outgo.id'))

    def __init__(self, arg):
        self.arg = arg


class Category(Base):
    """docstring for Categoria"""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)
    type = Column(Enum(TransactionType))

    def __init__(self, description, type):
        self.description = description
        self.type = type


class Income(Base):
    """docstring for Income"""
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True)
    value = Column(Numeric(asdecimal=False))
    description = Column(String(50))
    date = Column(DateTime)
    category_id = Column(Integer, ForeignKey('category.id'))

    def __init__(self, value, description, date, category):
        super(Income, self).__init__()
        self.value = value
        self.description = description
        self.date = date
        self.category_id = category.id


class Outgo(Base):
    """docstring for Outgo"""
    __tablename__ = 'outgo'
    id = Column(Integer, primary_key=True)
    value = Column(Numeric(asdecimal=False))
    description = Column(String(50))
    date = Column(DateTime)
    category_id = Column(Integer, ForeignKey('category.id'))

    def __init__(self, value, description, date, category):
        super(Outgo, self).__init__()
        self.value = value
        self.description = description
        self.date = date
        self.category_id = category.id


class CreditCard(object):
    __tablename__ = 'creditcard'
    id = Column(Integer, primary_key=True)
    limit = Column(Numeric(asdecimal=False))

    def __init__(self, limit, purchases):
        self.limit = limit
        self.purchases_id = purchases.id


engine = create_engine('sqlite:///:memory:', echo=True)
