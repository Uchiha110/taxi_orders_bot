import sqlite3

connection = sqlite3.connect('pub_loc.db')
cursor = connection.cursor()


async def actions_table(actions, name):
    table = """"""

    match actions:
        case "create":
            table = f"""CREATE TABLE [{name}] (
                            message_id   INTEGER (255) NOT NULL,
                            message_text TEXT          NOT NULL
                        );"""
        case "delete":
            table = f"""DROP TABLE [{name}]"""

    cursor.execute(table)


async def actions_chat_message(actions, table_name, message_id, message_text=False):
    table = """"""

    match actions:
        case "write":
            if message_text:
                query = f"INSERT INTO [{table_name}] (message_id, message_text) VALUES (?, ?)"
                cursor.execute(query, (message_id, message_text))

                connection.commit()
        case "delete":
            if not message_text:
                query = f"DELETE FROM [{table_name}] WHERE message_id = ?"
                cursor.execute(query, (message_id,))

                connection.commit()


async def get_name_table():
    table = """SELECT name FROM sqlite_master WHERE type='table';"""

    cursor.execute(table)
    tables = cursor.fetchall()

    return [table[0] for table in tables]

