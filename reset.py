from DB_connect import connect
from tkinter import messagebox, ttk
import psycopg2

def reset_base():
    '''
    Function resetting the database to its initial state.
    First, all tables are cascaded deleted, and then recreated with initial data.
    '''
    conn = connect()
    c = conn.cursor()

    # drop tables
    filepath_drop = 'sql/drop_tables.sql'
    with open(filepath_drop, 'r', encoding='utf-8') as fd:
        sql_file_drop = fd.read()

    sql_commands_drop = sql_file_drop.split(';')

    for command in sql_commands_drop:
        try:
            if command.strip() != '':
                c.execute(command)
        except Exception as e:
            print("Command skipped: ", e)

    conn.commit()
    conn.close()

    # create tables
    conn = connect()
    c = conn.cursor()
    filepath_create = 'sql/hotel.sql'
    with open(filepath_create, 'r', encoding='utf-8') as fd:
        sql_file_create = fd.read()

    sql_commands_create = sql_file_create.split(';')

    for command in sql_commands_create:
        try:
            if command.strip() != '':
                c.execute(command)
        except Exception as e:
            print("Command skipped: ", e)

    conn.commit()
    conn.close()

    conn = connect()
    c = conn.cursor()
    filepath_create = 'sql/triggers_and_functions.sql'
    with open(filepath_create, 'r', encoding='utf-8') as fd:
        sql_file_create = fd.read()

    sql_commands_create = sql_file_create.split('-- end')

    for command in sql_commands_create:
        try:
            if command.strip() != '':
                c.execute(command)
        except Exception as e:
            print("Command skipped: ", e)

    conn.commit()
    conn.close()
    messagebox.showinfo("Potwierdzenie", "Zresetowano bazę.")
