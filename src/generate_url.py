import random, string
from . import db_con
def generate_url():
    db = db_con.database_connection()
    random_num = random.randint(10000, 999999)
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k = 5))
    
    random_hexa = hex(random_num)
    
    url = random_str + str(random_hexa[2:])
    
    if db:
        curr = db.cursor()
        curr.execute("""SELECT * FROM urls WHERE short_url = '{url}' """)
        data = curr.fetchone()
        db.close()
        if data is not None:
            return generate_url(db)
        
    return url
    