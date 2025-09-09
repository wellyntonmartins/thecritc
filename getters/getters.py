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
    cursor = None

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

def search_rating_by_id(conn, id_game, id_user):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM ratings WHERE id_game = %s AND id_user = %s", (id_game, id_user,))
        rate_exists = cursor.fetchone();

        if rate_exists:
           return True, "Rate successfuly loaded", rate_exists
        else:
           return False, "Can't found. Rate don't exists in database", None
    except Exception as e:
        print(f'Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def average_rating_by_id(conn, id_game):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT AVG(rating) as avg FROM ratings WHERE id_game = %s", (id_game, ))
        average_rate = cursor.fetchone();

        return True, "Rate average successfuly loaded", average_rate
    except Exception as e:
        print(f'Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_comment(conn, id_game):
    cursor = None

    try:
        cursor = conn.cursor(dictionary=True, buffered=True)


        comments_infos = []
        cursor.execute("SELECT * FROM comments WHERE id_game = %s", (id_game, ))
        game_comments = cursor.fetchall();

        for comment in game_comments:
            cursor.execute("SELECT name FROM user WHERE id = %s", (comment['id_user'], ))
            name_user = cursor.fetchone()

            cursor.execute("SELECT rating FROM ratings WHERE id_user = %s AND id_game = %s", (comment['id_user'], comment['id_game'], ))
            rate_user = cursor.fetchone()

            comments_infos.append({
                "user_name": name_user['name'],
                "rate_user": rate_user['rating'],
                "comment_user": comment['comment']
            })


        return True, "Comments successfuly loaded", comments_infos
    except Exception as e:
        print(f'get_comment says: Something got wrong: {e}')
        return False, f'Something got wrong. Please contact the Admin', None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
