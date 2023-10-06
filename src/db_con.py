import sqlite3
def database_connection():
    conn = None
    try:
        conn = sqlite3.connect('databases/db.sqlite3')
        # print("Database connection established")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS urls(short_url VARCHAR(50) PRIMARY KEY, url VARCHAR(65550));''')
    except Exception as err:
        print(err)

    
    return conn


