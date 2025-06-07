from flask import Flask, g, render_template
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
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)


