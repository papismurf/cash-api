from flask import Flask, jsonify, request

from api.model.expense import Expense, ExpenseSchema
from api.model.income import Income, IncomeSchema
from api.model.transaction_type import TransactionType

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return 'Home'


incomes = [
    {'description': 'salary', 'amount': 120000}
]

app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


app.route('/incomes', methods=['POST'])
def add_income() -> tuple[str, int]:
    incomes.append(request.get_json())
    return '', 204


if __name__ == '__main__':
    app.run()
