import sqlite3

connection = sqlite3.connect('pub_loc.db')
cursor = connection.cursor()


def create_table(name):
    table = f"""CREATE TABLE [{name}] (
                message_id INTEGER (255) NOT NULL
            );"""

    cursor.execute(table)
