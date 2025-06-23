from flask import Flask, g, render_template, redirect, request
from before_request import connected_database

app = Flask(__name__)
app.secret_key = 'anySecretKey'

@app.before_request
def before_request_func():
     g.db = connected_database()
     g.cursor_arr = g.db.cursor(dictionary=False)
     g.cursor_dict = g.db.cursor(dictionary=True)
     print('Database sucessfully connected')

@app.after_request
def after_request_func(response):
    g.cursor_arr.close()
    g.cursor_dict.close()
    g.db.close()
    return response

@app.route('/')
def index():
    return redirect('/signin')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.json()

        email = data.get('email')
        password = data.get('password')

        # Here, will be the database connection to verify the user data

        return redirect('/home')
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        try:
            cursor = g.cursor_dict

            SQL = """
                INSERT INTO users (username, email, password) VALUES ( %s, %s, %s)
            """
            
            cursor.execute(SQL, (username, email, password))
            result = cursor.fetchall()
            print(f"\nPrint of the result: {result}")
            g.db.commit()

            message = "Your user has been created successfully!"
            return message, 200
        except Exception as e:
            print(f"Something failed: {e}")
            g.db.rollback()
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)


