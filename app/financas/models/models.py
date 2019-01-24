import enum
import os

from sqlalchemy import (Column, DateTime, Enum, ForeignKey, Integer, Numeric,
                        String, Table, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from werkzeug.security import generate_password_hash


class Tipo(enum.Enum):
    """Enum."""

    ENTRADA = 0
    SAIDA = 1


class MySession():

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
            base.metadata.bind = self._engine

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'


class Conta(Base):
    """docstring for Conta"""
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), unique=True)
    
    def __init__(self, descricao):
        self.descricao = descricao


class Transacao(Base):
    """docstring for Transacao"""
    __tablename__ = 'transacao'
    id = Column(Integer, primary_key=True)
    despesa_id = Column(Integer, ForeignKey('despesa.id'))

    def __init__(self, arg):
        super(Transacao, self).__init__()
        self.arg = arg


class Categoria(Base):
    """docstring for Categoria"""
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), unique=True)
    tipo = Column(Enum(Tipo))

    def __init__(self, arg):
        super(Categoria, self).__init__()
        self.arg = arg


class Renda(Base):
    """docstring for Renda"""
    __tablename__ = 'renda'
    id = Column(Integer, primary_key=True)
    valor = Column(Numeric(asdecimal=False))
    descricao = Column(String(50))
    data = Column(DateTime)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    def __init__(self, arg):
        super(Renda, self).__init__()
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.categoria_id = categoria.id


class Despesa(Base):
    """docstring for Despesa"""
    __tablename__ = 'despesa'
    id = Column(Integer, primary_key=True)
    valor = Column(Numeric(asdecimal=False))
    descricao = Column(String(50))
    data = Column(DateTime)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    def __init__(self, valor, descricao, data, categoria):
        super(Despesa, self).__init__()
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.categoria_id = categoria.id


class Cartao(Base):
    """docstring for Cartao"""
    __tablename__ = 'cartao'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), unique=True)
    limite = Column(Numeric(asdecimal=False))
    vencimento = Column(DateTime)

    def __init__(self, arg):
        super(Cartao, self).__init__()
        self.arg = arg


class Saldo(Base):
    """docstring for Saldo"""
    __tablename__ = 'saldo'
    id = Column(Integer, primary_key=True)
    saldo = Column(Numeric(asdecimal=False))
    data = Column(DateTime)

    def __init__(self, arg):
        super(Saldo, self).__init__()
        self.arg = arg
