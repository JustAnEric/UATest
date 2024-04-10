import sqlite3, os, random, encryption

db = sqlite3.connect('lite.db', check_same_thread=False)
cursor = db.cursor()

def create_table(table_name):
    db.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL UNIQUE
    );
    ''')
    db.commit()
    
def delete_table(table_name):
    db.execute(f'DROP TABLE IF EXISTS {table_name}')
    db.commit()
    
def write_to_table(table_name, vals=list[tuple]):
    db.executemany(f'INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)', vals)
    db.commit()
    
def create_user(
    email:str,
    password:str,
    firstName:str,
    lastName:str
):
    uid = random.randint(0,100000000)
    
    # write the user to the users table
    
    create_table('users') # just try and create the table first
    write_to_table('users', 
        [(str(uid), str(firstName), str(lastName), str(encryption.hash(email)), str(encryption.hash(password)))]
    )

    return uid

def remove_user(
    uid:str
):
    query = f"DELETE FROM users WHERE id={uid}"
    try:
        db.execute(query)
        db.commit()
    except Exception as e:
        print(e.with_traceback())
        return False
    
    return True
    
def get_users():
    create_table('users')
    cursor.execute(f"SELECT * FROM users")
    rows = cursor.fetchall()
    return rows

def user(tuplwe,email):
    for user in tuplwe:
        print(user)
        if encryption.check_hash(str(email).encode("UTF-8"), str(user[3]).encode("UTF-8")):
            return user
    
    return None