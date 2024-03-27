from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/seafood/<int:id>')
def seafood(id):


    conn = sqlite3.connect('seafood.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE id=?',(id,))
    seafood = cur.fetchone()
    return render_template('seafood.html', seafood=seafood)


if __name__ == "__main__":
    app.run(debug=True)