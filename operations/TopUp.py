import random
from flask import jsonify, request
from flask_restful import Resource


class TopUp(Resource):
    def post(self, resource):
        """
            Top up user account
            Call this api passing an user id and amount of money you want to send to the account
            ---
            tags:
              - Top up
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
                description: Amount of monet to top-up
            responses:
              500:
                description: Fatal error
              401:
                description: Incorrect user id
              402:
                description: Operation could not be executed
              200:
                description: Account topped-up successfully
                schema:
                  type: object
                  required:
                    - userid
                    - amount
                  id: top_up
                  properties:
                    amount:
                      type: number
                      example: 124.5
                    user_id:
                      type: string
                      format: uuid
                      example: d290f1ee-6c54-4b01-90e6-d701748f0851

            """
        topup_successful = True

        #TODO:
        # add money to account in database

        if topup_successful:
            return jsonify({
                {"status": "top-up successful"}, {"date": "23-10-2019Z15:25"}, {"user_id": "232354334ud"},
                {"amount": "54213454"},
            }
            )
        else:
            return jsonify({
                {"status": "top-up unsuccessful"}
            }
            )