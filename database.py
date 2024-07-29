import sqlite3

connection1 = sqlite3.connect('pub_loc.db')
connection2 = sqlite3.connect('uuid_order.db')
cursor1 = connection1.cursor()
cursor2 = connection2.cursor()


async def actions_table(actions, name):
    table = """"""

    match actions:
        case "create":
            table = f"""CREATE TABLE [{name}] (
                            uuid_order   TEXT    NOT NULL,
                            message_id   INTEGER NOT NULL,
                            message_text TEXT    NOT NULL
                        );"""
        case "delete":
            table = f"""DROP TABLE [{name}]"""

    cursor1.execute(table)


async def actions_chat_message(actions, table_name, uuid_order, message_id, message_text=False):
    match actions:
        case "write":
            if message_text:
                query = f"INSERT INTO [{table_name}] (uuid_order, message_id, message_text) VALUES (?, ?, ?)"
                cursor1.execute(query, (uuid_order, message_id, message_text))

                connection1.commit()
        case "delete":
            if not message_text:
                query = f"DELETE FROM [{table_name}] WHERE uuid_order = ?"
                cursor1.execute(query, (uuid_order,))

                connection1.commit()


async def get_name_table():
    table = """SELECT name FROM sqlite_master WHERE type='table';"""

    cursor1.execute(table)
    tables = cursor1.fetchall()

    return [table[0] for table in tables]


# async def get_uuid_order_table(name):
#     table = f"""SELECT uuid_order FROM [{name}]"""
#
#     cursor1.execute(table)
#     tables = cursor1.fetchall()
#
#     return [table[0] for table in tables]


async def get_message_id_table(name, uuid_order):
    query = f"""SELECT message_id FROM [{name}] WHERE uuid_order = ?"""
    cursor1.execute(query, (uuid_order,))

    tables = cursor1.fetchall()

    return [table[0] for table in tables]


async def get_message_text_table(name, uuid_order):
    query = f"""SELECT message_text FROM [{name}] WHERE uuid_order = ?"""
    cursor1.execute(query, (uuid_order,))

    tables = cursor1.fetchall()

    return [table[0] for table in tables]


async def add_uuid_order(uuid_):
    query = """INSERT INTO uuid_order_ (uuid_) VALUES (?)"""
    cursor2.execute(query, (uuid_,))

    connection2.commit()


async def get_uuid_order():
    table = """SELECT uuid_ FROM uuid_order_"""

    cursor2.execute(table)
    tables = cursor2.fetchall()

    return [table[0] for table in tables]


async def del_uuid_order(name, uuid):
    query1 = f"""DELETE FROM [{name}] WHERE uuid_order = ?"""
    cursor1.execute(query1, (uuid,))
    connection1.commit()

    query2 = """DELETE FROM uuid_order_ WHERE uuid_ = ?"""
    cursor2.execute(query2, (uuid,))
    connection2.commit()
