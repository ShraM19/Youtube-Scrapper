import sqlite3

def create_db()
    #conn=sqlite3.connect(':memory:')
    conn=sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("CREATE TABLE customers(first_name text,last_name text,email text)")
    conn.commit()
    conn.close()

def insert_table()
    conn=sqlite3.connect('customer.db')
    c = conn.cursor()
    many_vid=[

    ]

    c.executemany("INSERT INTO videos VALUES(?,?,?)",many_vid)
    print("Command successfully executed")
    conn.commit()
    conn.close()


