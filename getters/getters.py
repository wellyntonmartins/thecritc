from flask import session
import hashlib

# search user in database for signin
def search_user(conn, user_email, user_password):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)

        SQL = "SELECT * FROM user WHERE email = %s"

        values = (user_email, )

        cursor.execute(SQL, values)
        user_record = cursor.fetchone()

        if user_record:
           comp_password = hashlib.md5(user_password.encode()).hexdigest()

           if comp_password == user_record["password"]:
              session['id'] = user_record["id"]          
              session['user'] = user_record["email"]  
              session['name'] = user_record["name"]        
              session['password'] = user_record["password"]   
              session.permanent = True
              return True, 'User success logged!', session
           else:
              return False, 'Wrong credentials. Please try again', None
        else:
           return False, "Can't found user. Please create a account before enter on theCritic", None
    except Exception as e:
        print(f'Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_database_game(conn):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)

        SQL = "SELECT * FROM game"

        cursor.execute(SQL)
        game_record = cursor.fetchall()

        if game_record:
           return True, "Games successfuly loaded", game_record
        else:
           return False, "Can't found games. Please contact the support", None
    except Exception as e:
        print(f'Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def game_by_id(conn, id):
    try:
        cursor = conn.cursor(dictionary=True)

        SQL = "SELECT * FROM game WHERE id = %s"

        values = (id,)

        cursor.execute(SQL, values)
        game_record = cursor.fetchone()

        if game_record:
           return True, "Game successfuly loaded", game_record
        else:
           return False, "Can't found game. Please contact the support", None
    except Exception as e:
        print(f'Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()