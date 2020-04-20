import sqlite3

def create_tables(conn):
    statements = []
    statements.append('''CREATE TABLE people
        (id integer primary key, name text, email text, phone text)
    ''')
    statements.append('''CREATE TABLE institutions
        (id integer primary key, name text, website text, street text, city text, state text, country text )
    ''')
    statements.append('''CREATE TABLE department
        (id integer primary key, name text, website text, inst_id integer)
    ''')
    statements.append('''CREATE TABLE lab
        (id integer primary key, name text, website text, dept_id integer)
    ''')
    statements.append('''CREATE TABLE project
        (id integer primary key, name text, website text, type text)
    ''')
    for st in statements:
        try:
            conn.execute(st)
        except:
            import pdb ; pdb.set_trace()

def execute_this(conn, list_of_statements):
    for st in list_of_statements:
        try:
            conn.execute(st)
        except:
            import pdb ; pdb.set_trace()

def populate_people():
    pass

def populate_institutions():
    pass

def populate_projects():
    pass

def populate_lab():
    pass


if __name__ == "__main__":
    conn = sqlite3.connect("whoswho.db")
    #create_tables(conn)