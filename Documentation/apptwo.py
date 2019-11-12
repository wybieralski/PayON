import os

import flask
from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
from flasgger import Swagger
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from datetime import datetime
from database_setup import Base, User, Accounts, Transactions
import google_auth
import google.oauth2.credentials
import googleapiclient.discovery

# Database
# Connect to Database and create database session
engine = create_engine('sqlite:///payment_service.db',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.bind = engine
app = flask.Flask(__name__)
api = Api(app)
swagger = Swagger(app)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        add_user(user_info)
        session.rollback()
        user_email = str(user_info['email'])
        new_balance = session.query(Accounts).filter_by(email=user_email).one()
        # balance = session.query(Accounts).filter_by(email=user_info['email']).one().balance
        # print(balance)
        return flask.render_template('logged.html', user_info=google_auth.get_user_info(),balance=new_balance.balance)
        # return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"
    else:
        session.close()
        return flask.render_template('login.html')


@app.route('/info')
def info():
    if google_auth.is_logged_in():
        session.rollback()
        user_info = google_auth.get_user_info()
        user_email = str(user_info['email'])
        # balance = session.query(Accounts).filter_by(email=user_email).one()
        # nb = balance.balance
        # request.form['name']
        new_balance = session.query(Accounts).filter_by(email=user_email).one()
        print(new_balance.email)
        return flask.render_template('info.html', user_info=google_auth.get_user_info(),balance=new_balance.balance)
        # return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    return flask.render_template('login.html')



def add_user(user_info):
    try:
        print(user_info['id'], user_info['email'])
        iddb = str(user_info['id'])
        emaildb = user_info['email']
        user = User(id=iddb, email=emaildb)
        account = Accounts(email=emaildb, balance=0)
        session.add(user)
        session.add(account)
        session.commit()

        print("RECORD SUCCESFULLY ADDED")
        print("ACCOUNT SUCCESFULLY CREATED")

    except:
        print("ERROR: RECORD NOT ADDED")


@app.route('/cred')
def cred():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()

        return flask.render_template('list.html', user_info)

    return 'You are not currently logged in.'


# @app.route('/top_up')
# def top_up():
#     if google_auth.is_logged_in():
#         return render_template("topup.html", user_info=google_auth.get_user_info())
#     else:
#         return flask.render_template('login.html')




@app.route('/transaction', methods=['GET', 'POST'])
def transactions():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        user_email = str(user_info['email'])
        transactions = session.query(Transactions).filter_by(account_mail=user_email).all()
        for transaction in transactions:
            print(transaction['amount'])
        # amount = session.query(Transactions).filter_by(account_mail=user_email).amount
        # date = session.query(Transactions).filter_by(account_mail=user_email).date
        # transaction_id = session.query(Transactions).filter_by(account_mail=user_email).transaction_id
        return render_template("transaction.html", user_info=google_auth.get_user_info())        
        # return render_template("transaction.html", user_info=google_auth.get_user_info(),transaction_description=transaction_description,amount=amount,date=date,transaction_id=transaction_id)
    else:
        return flask.render_template('login.html')



@app.route('/top_up', methods=['GET', 'POST'])
def top_up():
    if request.method == 'POST':
        user_info = google_auth.get_user_info()
        user_email = str(user_info['email'])
        balance = session.query(Accounts).filter_by(email=user_email).one()
        nb = balance.balance
        amount  = request.form['amount']
        # request.form['name']
        new_balance = session.query(Accounts).filter_by(email=user_email).one()
        print(new_balance.email)
        new_amount = int(new_balance.balance) + int(amount)
        new_balance.balance = new_amount
        session.commit()
        # session.close()

        return jsonify({"status": "works","amount": new_amount,"id":new_balance.email})
    else:
        if google_auth.is_logged_in():
            return render_template("topup.html",user_info=google_auth.get_user_info())
        else:
            return flask.render_template('login.html')

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        user_info = google_auth.get_user_info()
        user_email = str(user_info['email'])
        amount  = request.form['amount']
        title  = request.form['title']
        bank_account  = request.form['account_nr']
        #decrease balance
        balance = session.query(Accounts).filter_by(email=user_email).one()
        new_balance = balance.balance - int(amount)
        if new_balance<0:
            return jsonify({"status": "failed","info":"you dont have enough money. Top up your account"})
        balance.balance = new_balance
        transaction = Transactions(account_mail=user_email, receiver_bank_account=bank_account,transaction_description=title,amount=amount)
        session.add(transaction)
        session.commit()
        transaction_title = jsonify({"Title":"sometitle"})
        
        return jsonify({"status": "works"})
    else:
        if google_auth.is_logged_in():
            return render_template("pay.html",user_info=google_auth.get_user_info())
        else:
            return flask.render_template('login.html')

# @app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In')


@app.route('/api/topup', methods=['POST'])
def top_up_post():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return jsonify(
            {"name": str(user_info['given_name'])},
            {"status": "POST TASK successful"},
            {"date": "23-10-2019Z15:25"},
            {"userid": request.json['userid']},
            # {"buyer_id": request.json['userid']},
            {"seller_id": "2sd324334ud"},
            {"date": str(datetime.now())},
            {"transaction_id": "54213454"})
    else:
        return jsonify(
            {"status": "top up unsuccessful"},
        )


@app.route('/api/payment/<userid>', methods=['GET'])
def get_payment():
    return jsonify({
        {"status": "GET payment successful"},
        {"date": "23-10-2019Z15:25"},
        {"buyer_id": "232354334ud"},
        {"seller_id": "2sd324334ud"},
        {"transaction_id": "54213454"}})


# curl -X GET "http://localhost:8040/api/payment"
@app.route('/api/payment', methods=['GET'])
def payment():
    if request.method == 'GET':
        token = request.json['token']
        return jsonify({
            "status": "GET payment successful",
            "token": token,
            "date": "23-10-2019Z15:25",
            "buyer_id": "232354334ud",
            "seller_id": "2sd324334ud",
            "transaction_id": "54213454"}
        )
    if request.method == 'POST':
        return jsonify({
            "status": "POST payment successful",
            "date": "23-10-2019Z15:25",
            "buyer_id": "232354334ud",
            "seller_id": "2sd324334ud",
            "transaction_id": "54213454"}
        )

    # return jsonify({"buyer_id": "sample",
    #                 "transaciton_id": "sample",
    #                 "date": "sample",
    #                 "seller_account": "sample"
    #                 })


@app.route('/api/payment/', methods=['GET'])
def get_payments():
    return jsonify({
        {"status": "GET payment successful"},
        {"date": "23-10-2019Z15:25"},
        {"buyer_id": "232354334ud"},
        {"seller_id": "2sd324334ud"},
        {"transaction_id": "54213454"}})


@app.route('/api/transaction/<userid>', methods=['GET'])
def get_transaction():
    return jsonify({
        {"status": "GET transaction successful"},
        {"date": "23-10-2019Z15:25"},
        {"buyer_id": "232354334ud"},
        {"seller_id": "2sd324334ud"},
        {"transaction_id": "54213454"}})

    # return jsonify({"buyer_id": "sample",
    #                 "transaciton_id": "sample",
    #                 "date": "sample",
    #                 "seller_account": "sample"
    #                 })


@app.route('/api/transaction/', methods=['GET'])
def get_transactions():
    return jsonify({
        {"status": "GET transaction successful"},
        {"date": "23-10-2019Z15:25"},
        {"buyer_id": "232354334ud"},
        {"seller_id": "2sd324334ud"},
        {"transaction_id": "54213454"}})

    # return jsonify({"buyer_id": "sample",
    #                 "transaciton_id": "sample",
    #                 "date": "sample",
    #                 "seller_account": "sample"
    #                 })


@app.route('/api/transaction/<userid>', methods=['POST'])
def create_transaction():
    if not request.json or not 'userid' in request.json:
        abort(400)
    return jsonify({
        {"status": "POST transaction successful"},
        {"date": "23-10-2019Z15:25"},
        {"buyer_id": "232354334ud"},
        {"seller_id": "2sd324334ud"},
        {"transaction_id": "54213454"}})


# app.run(debug=True)


def create_account(user_info):
    try:
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        print(user_info['id'], user_info['email'])
        iddb = str(user_info['id'])
        account = Accounts(id_account=iddb, balance=0)
        session.add(account)
        session.commit()
        print("ACCOUNT SUCCESFULLY CREATED")
    except:
        print("ERROR:ACCOUNT NOT CREATED")
