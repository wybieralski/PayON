import random
from flask import jsonify, request
from flask_restful import Resource


class AllTransactions(Resource):
    def get(self):
        """
                   Returns all the transactions
                   ---
                   responses:
                     200:
                       description: Returns all transactions
                    """

        features = [
            {"payment_id": "2354334ud"}, {"date": "23-10-2019Z15:25"}, {"buyer_id": "232354334ud"},
            {"seller_id": "2sd324334ud"},
        ]
        size = int(request.args.get('size', 1))

        return jsonify(
            features=random.sample(features, size)
        )