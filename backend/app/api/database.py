
def database_action_file(file):
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
    try:
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()

def database_action_script(script):
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
    try:
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
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



