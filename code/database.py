import sqlite3

conn = sqlite3.connect('api_data.db')
cursor = conn.cursor()

# Drop Table is exist
cursor.execute('''DROP TABLE IF EXISTS users''')
cursor.execute('''DROP TABLE IF EXISTS items''')

# Create table with Coloum ID will be AUTOINCREMENT
create_table = '''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    username TEXT,
                    password TEXT
                    )'''
cursor.execute(create_table)

create_table = '''CREATE TABLE items(
                    name TEXT,
                    price FLOAT
                    )'''
cursor.execute(create_table)
print("Table Created Successfully: ")


conn.commit()

select_Script = '''select * from users'''
abc = conn.execute(select_Script)
for data in abc:
    print(data)
conn.close()
