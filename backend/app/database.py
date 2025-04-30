
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

def database_query_script(script) -> list:
    import psycopg2 
    conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="1.6180339",
                        port="9999")
    cursor = conn.cursor()
    cursor.execute(script)
    output = cursor.fetchall()
    print(cursor.fetchall())
    conn.commit()
    cursor.close()
    conn.close()
    return output
    

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

def database_get_columns(table):
    query = f"SELECT * FROM {table} LIMIT 0" 
    import psycopg2 
    conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="1.6180339",
                        port="9999")
    cursor = conn.cursor()
    cursor.execute(query)
    output = [des[0] for des in cursor.description]
    conn.commit()
    cursor.close()
    conn.close()
    return output


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



