
def database_query(file):
    import psycopg2 
    conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="1.6180339",
                        port="9999")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        strfile = f.read()
        cursor.execute(strfile)
        print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()

def database_insert(table, *args):
    query = f"INSERT INTO {table} VALUES {args};"
    
    import psycopg2 
    conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="1.6180339",
                        port="9999")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def init_table(file):
    import psycopg2 
    conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="1.6180339",
                        port="9999")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        strfile = f.read()
        cursor.execute(strfile)
    conn.commit()
    cursor.close()
    conn.close()


init_table('createTable.sql')
