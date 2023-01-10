import datetime as dt

from marshmallow import Schema, fields


class Transaction(object):
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.transaction_type = transaction_type

    def __repr__(self):
        return f"<Transacttion(name={self.description!r})>"


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    transaction_type = fields.Str()

