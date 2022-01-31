from typing import Dict, Tuple

from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be left blank!"
    )

    def post(self) -> Tuple[Dict[str, str], int]:
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username already exists."}, 400

        user = UserModel(**data)

        try:
            user.save_to_db()
        except Exception as e:
            return {"message", "An error ocurred creating the user."}, 500

        return {"message": "User created successfully"}, 201
