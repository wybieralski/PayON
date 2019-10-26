import random
from flask import jsonify, request
from flask_restful import Resource


class AllPayments(Resource):
    def get(self):
        """
                   Returns all the payments
                   ---
                   responses:
                     200:
                       description: Returns all payments
                    """

        features = [
            {"payment_id": "2354334ud"}, {"date": "23-10-2019Z15:25"}, {"t_id": "5463322"},
        ]
        size = int(request.args.get('size', 1))

        return jsonify(
            features=random.sample(features, size)
        )