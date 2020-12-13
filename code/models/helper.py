import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('Api_data.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM users where username = ?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone() # if there is no result for above query then it will (row=None)

        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('Api_data.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM users WHERE id = ?"
        result = conn.execute(select_query, (_id,))
        row = result.fetchone()
        if row:
            user_id = cls(*row)
        else:
            user_id = None

        conn.close()
        return user_id
