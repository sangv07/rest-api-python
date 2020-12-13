import sqlite3

class Utilities:

    # to contain object properties of internal method
    def __init__(self):
        pass

    @classmethod
    def db_connection(cls):
        conn = sqlite3.connect('Api_data.db')
        cursor = conn.cursor()
        return conn, cursor

    @classmethod
    def find_by_name(cls, name):
        conn, cursor = cls.db_connection()

        select_query = "SELECT * FROM items where name = ?"
        result = cursor.execute(select_query, (name,))
        row = result.fetchone()
        conn.close()
        print("row from find_By_name: ", row)

        if row:
            return {'item':{'name': row[0], 'price': row[1]}}

    @classmethod
    def insert(cls, item):
        conn, cursor = cls.db_connection()

        insert_query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(insert_query, (item['name'], item['price']))

        conn.commit()
        conn.close()

    @classmethod
    def update(cls, item):
        conn, cursor = cls.db_connection()

        update_query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(update_query, (item['price'], item['name']))

        conn.commit()
        conn.close()
