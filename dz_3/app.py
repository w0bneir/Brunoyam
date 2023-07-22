from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

def connect_db():
    con = sql.connect('soc.db')
    con.row_factory = sql.Row
    return con

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        con = connect_db()
        cur = con.cursor()
        cur.execute('''INSERT INTO Users (username, email, password, first_name, last_name)
                        VALUES (?, ?, ?, ?, ?)''', (username, email, password, first_name, last_name))
        con.commit()
        con.close()

        return "User added successfully!"

if __name__ == '__main__':
    app.run(debug=True)