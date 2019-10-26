from operations.TopUp import TopUp
from operations.Payment import Payment
from operations.Transaction import Transaction
from operations.GetAllTransactions import AllTransactions
from operations.GetAllPayments import AllPayments

from flask import Flask, redirect, render_template, url_for
from flasgger import Swagger
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


api.add_resource(TopUp, '/topup/<username>')
api.add_resource(Payment, '/payment/<username>')
api.add_resource(Transaction, '/transaction/<username>')
api.add_resource(AllTransactions, '/transactions/')
api.add_resource(AllPayments, '/payments')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In')


app.run(debug=True)
