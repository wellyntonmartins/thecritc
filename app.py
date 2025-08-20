from flask import Flask, g, render_template, redirect, request, session, flash
import mysql.connector 
from mysql.connector import Error
from connection import config
from getters import getters # Getters for database
from setters import setters # Setters for database

app = Flask(__name__)
app.secret_key = 'anySecretKey'

@app.route('/')
def index():
    return redirect('/home')

# Enter in home page
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('signin')
    conn = mysql.connector.connect(**config)
    
    success, message, games = getters.get_database_game(conn)

    if success == True:
        return render_template('home.html', games=games)
    else:
        flash(f'\n {message}', 'danger')
        return render_template('home.html')

# Enter in signin page
@app.route('/signin', methods=['GET'])
def signin():
    return render_template('signin.html')

# Auth in theCritic
@app.route('/auth', methods=['POST'])
def auth():
    conn = mysql.connector.connect(**config)

    user_email = request.form['email']
    user_password = request.form['password']

    success, message, session = getters.search_user(conn, user_email, user_password)

    if success == True:
        flash(message, 'success')

        session = session
        return redirect('home')
    else:
        flash(f'\n {message}', 'danger')
        return redirect('signin')

# Register in theCritic
@app.route('/register', methods=['POST'])
def register():
    conn = mysql.connector.connect(**config)

    user_name = request.form['username']
    user_email = request.form['email']
    user_password = request.form['password']

    success, message= setters.insert_user(conn, user_name, user_email, user_password)

    if success == True:
        flash(message, 'success')
        return redirect('signin')
    else:
        flash('Something got erong. Please, contact the admin.', 'error')
        print(message)
        return redirect('signup')

# Enter on signup page
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('signin')

@app.route('/gamepage', methods=['POST'])
def gamepage():
    if 'user' not in session:
        return redirect('signin')
    
    conn = mysql.connector.connect(**config)

    id_game = request.form['game_id']

    success, message, game = getters.game_by_id(conn, id_game)

    if success == True:
        flash(message, 'success')
        return render_template('gamepage.html', game=game)
    else:
        flash('Something got wrong. Please, contact the admin', 'error')
        print(message)
        return redirect('home')


if __name__ == '__main__':
    app.run(debug=True)


