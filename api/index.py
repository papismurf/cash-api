from flask import Flask, jsonify, request

from api.model.expense import Expense, ExpenseSchema
from api.model.income import Income, IncomeSchema
from api.model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
    Income('Remittance', 5000),
    Income('Dividends', 200),
    Income('Dinner', 50),
    Expense('Travel', 100)
]

@app.route('/')
def home():  # put application's code here
    return 'Home'


app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)


app.route('/incomes', methods=['POST'])
def add_income() -> tuple[str, int]:
    income = IncomeSchema.load(request.get_json())
    transactions.append(income)
    return '', 204

app.route('/expenses')
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 204


if __name__ == '__main__':
    app.run()
