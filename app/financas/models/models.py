import os

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        String, Table, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from werkzeug.security import generate_password_hash

class MySession():

    def __init__(self, base, test=False):
        """Inicializa."""
        if test:
            path = ':memory:'
        else:
            path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'sqlite.db')
            print('***Banco de Dados...', path)
            if os.name != 'nt':
                path = '/' + path
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


class SQLDBUser(Base):
    """Base de Usuários."""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    _password = Column(String(200))

    def __init__(self, username, password):
        """Inicializa."""
        self.username = username
        self._password = self.encript(password)

    @classmethod
    def encript(self, password):
        """Recebe uma senha em texto plano, retorna uma versão encriptada."""
        return generate_password_hash(password)

    @classmethod
    def get(cls, session, username, password=None):
        """Testa se usuário existe, e se passado, se a senha está correta.

        Returns:
            SQLDBUser ou None

        """
        if password:
            DBUser = session.query(SQLDBUser).filter(
                SQLDBUser.username == username,
                SQLDBUser._password == cls.encript(password)
            ).first()
        else:
            DBUser = session.query(SQLDBUser).filter(
                SQLDBUser.username == username,
            ).first()
        return DBUser


class Transacao(Base):
    """docstring for Transacao"""
    __tablename__ = 'transacao'
    id = Column(Integer, primary_key=True)

    def __init__(self, arg):
        super(Categoria, self).__init__()
        self.arg = arg


class Categoria(Base):
    """docstring for Categoria"""
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(30), unique=True)

    def __init__(self, arg):
        super(Categoria, self).__init__()
        self.arg = arg
        

class Renda(Base):
    """docstring for Renda"""
    __tablename__ = 'renda'
    id = Column(Integer, primary_key=True)
    valor = Column(Numeric(asdecimal=False))
    data = Column(DateTime)

    def __init__(self, arg):
        super(Renda, self).__init__()
        self.arg = arg


class Despesa(Base):
    """docstring for Despesa"""
    __tablename__ = 'despesa'
    id = Column(Integer, primary_key=True)
    valor = Column(Numeric(asdecimal=False))
    data = Column(DateTime)

    def __init__(self, arg):
        super(Despesa, self).__init__()
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
