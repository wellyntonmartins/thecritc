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

def insert_note(conn, id_game, id_user, rating):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM ratings WHERE id_game = %s AND id_user = %s", (id_game, id_user,))
        rate_exists = cursor.fetchone();

        if rate_exists: 
            SQL_UPDATE = "UPDATE ratings SET rating = %s WHERE id_game = %s AND id_user = %s"
            values_update = (rating, id_game, id_user,)
            cursor.execute(SQL_UPDATE, values_update)
        else:
            SQL = "INSERT INTO ratings (id_game, id_user, rating) VALUES (%s, %s, %s)"
            values = (id_game, id_user, rating,)
            cursor.execute(SQL, values)
        
        conn.commit()
        
        return True, f'Rate {rating} successfuly registered'
    except Exception as e:
        if conn:
            conn.rollback()
        return False, f'\nSomething got wrong: {e}'
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()