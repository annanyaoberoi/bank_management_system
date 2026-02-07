from flask import Flask, request, jsonify
from flask_cors import CORS   
from db import create_account, record_transaction, get_balance, get_statement

app = Flask(__name__)
CORS(app) 

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    create_account(
        int(data['acc_no']),
        name=data['name'],
        dob=data['dob'],
        address=data['address'],
        mob_no=int(data['mob_no']),
        initial_balance=float(data['initial_balance'])
    )
    return jsonify({'message': '✅ Account created successfully.'})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    record_transaction(
        int(data['acc_no']),
        'deposit',
        float(data['amount'])
    )
    return jsonify({'message': '✅ Deposit successful.'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    record_transaction(
        int(data['acc_no']),
        'withdraw',
        float(data['amount'])
    )
    return jsonify({'message': '✅ Withdraw successful.'})

@app.route('/balance', methods=['POST'])
def balance():
    data = request.json
    bal = get_balance(int(data['acc_no']))
    return jsonify({'message': f'🗒 Current Balance: {bal}'})

@app.route('/statement', methods=['POST'])
def statement():
    data = request.json
    stmt = get_statement(int(data['acc_no']))
    return jsonify({'message': stmt})

if __name__ == "__main__":
    app.run(debug=True)
