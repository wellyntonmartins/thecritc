import hashlib

# insert user on database to signup
def insert_user(conn, name, email, password):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)
        
        password_hash = hashlib.md5(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        user_exists = cursor.fetchone()

        if user_exists:
            return False, 'Email already exists in theCritic. Please, select other!'
        
        SQL = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password_hash)

        cursor.execute(SQL, values)
        conn.commit()
        
        return True, 'User success registered'
    except Exception as e:
        if conn:
            conn.rollback()
        return False, f'\nSomething got wrong: {e}'
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()