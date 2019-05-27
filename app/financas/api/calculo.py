from app.financas.models.models import (Account, Category, CreditCard,
                                        Transaction, User)


class Calculo:

    def create_category(description: str):
        category = Category(description)
        dbsession.add(category)
        dbsession.commit()

    def add_transaction(description, value, date, payed_with, parcels, category, transaction_type):
        transaction = Transaction(description, value, date,
                                  payed_with, parcels, category, transaction_type)
        dbsession.add(transaction)
        dbsession.commit()
