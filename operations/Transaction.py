import random
from flask import jsonify, request
from flask_restful import Resource


class Transaction(Resource):
    def get(self, userid):
        """
                   Returns payment for specified user
                   ---
                   parameters:
                     - in: path
                       name: userid
                       type: string
                       required: true
                   responses:
                     200:
                       description: A single user item
                       schema:
                         id: User
                         properties:
                           username:
                             type: string
                             description: The name of the user
                             default: Steven Wilson
                    """
        features = [
            {"payment_id": "2354334ud"}, {"date": "23-10-2019Z15:25"}, {"buyer_id": "232354334ud"},
            {"seller_id": "2sd324334ud"},
        ]
        size = int(request.args.get('size', 1))

        return jsonify(
            features=random.sample(features, size)
        )

    def post(self, userid):
        """
            Creates transaction for payment
            Call this api passing an user id and amount of money you want to send to the account
            ---
            tags:
              - Transaction
            parameters:
              - name: userid
                in: path
                type: uuid
                required: true
                description: User Id
              - name: amount
                in: query
                required: true
                type: integer
                description: Amount of money to pay
              - name: seller
                in: query
                required: true
                type: integer
                description: Name of receiving account
            responses:
              500:
                description: Fatal error
              401:
                description: Incorrect user id
              402:
                description: Operation could not be executed
              200:
                description: Payment successful
                schema:
                  type: object
                  required:
                    - userid
                    - amount
                    - seller
                  id: transaction
                  properties:
                    amount:
                      type: number
                      example: 124.5
                    user_id:
                      type: uuid
                      example: d290f1ee-6c54-4b01-90e6-d701748f0851
                    seller_id:
                      type: uuid
                      example: d290f1ee-6c54-4b01-90e6-d701748f0851

            """
        #TODO:
        # check if paayment is successful

        payment_successful = True
        if payment_successful:
            return jsonify({
                {"status": "transaction successful"}, {"date": "23-10-2019Z15:25"}, {"buyer_id": "232354334ud"},
                {"seller_id": "2sd324334ud"}, {"transaction_id": "54213454"},
            }
            )
        else:
            return jsonify({
                {"status": "transaction did not happen"}
            }
            )




