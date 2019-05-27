from flask import current_app

from app.financas.models.models import (Account, Category, CreditCard,
                                        Transaction, User)


class Registration(object):

    def set_session(self):
        """Recebe conexão."""
        self.dbsession = current_app.config.get('dbsession')

    def user_registration(username: str, password: str):
        user = User(username, password)
        dbsession.add(user)
        dbsession.commit()

    def create_account(bank: str, description: str, balance: str, user: User):
        account = Account(description, bank, balance, user)
        dbsession.add(account)
        dbsession.commit()

    def add_creditcard(limit: float, account: Account, date_pay: datetime):
        creditcard = CreditCard(limit, account, date_pay)
        dbsession.add(creditcard)
        dbsession.commit()
