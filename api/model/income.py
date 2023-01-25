from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Income(Transaction):
    def __int__(self, description, amount):
        super(Income, self).__int__(desscription, amount, TransactionType.INCOME)

    def __repr__(self):
        return f'<Income(name={self.description!r}>'
        pass


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)

