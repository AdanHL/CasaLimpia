from flask_login import UserMixin
from app.db import get_db


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, userdata):
        """
        :param user_data : UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        db = get_db()
        user = db.execute(f"SELECT username, password FROM users WHERE id={user_id}").fetchone
        user_data = UserData(
            username = user[0],
            password = user[1]
        )
        return UserModel(user_data)