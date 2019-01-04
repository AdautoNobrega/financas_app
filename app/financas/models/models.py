import os

from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
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

class Transacoes(Base):
    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True)
