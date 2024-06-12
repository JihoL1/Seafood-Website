from flask import Flask, render_template
import sqlite3
db = 'seafood.db'
app = Flask(__name__)


#homepage
@app.route('/')
def homepage():
    return render_template('/method/home.html')


#steaming
@app.route('/steaming')
def steaming():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    for row in cur.execute('SELECT name, description, image FROM Seafood WHERE method ="1"'):
        row = cur.fetchall()
        return render_template('/method/steaming.html', row=row)


#frying
@app.route('/frying')  
def frying():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE Method = "2"')
    frying = cur.fetchone()
    return render_template('/method/frying.html', frying=frying)


#raw
@app.route('/raw')  
def raw():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=3')
    raw = cur.fetchone()
    return render_template('/method/raw.html', raw=raw)


#grilling
@app.route('/grilling')  
def grilling():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=4')
    grilling = cur.fetchone()
    return render_template('/method/grilling.html', grilling=grilling)


#baking
@app.route('/baking')  
def baking():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=5')
    baking = cur.fetchone()
    return render_template('/method/baking.html', baking=baking)


#poaching
@app.route('/poaching')  
def poaching():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=6')
    poaching = cur.fetchone()
    return render_template('/method/poaching.html', poaching=poaching)


#barbecuing
@app.route('/barbecuing')  
def barbecuing():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=7')
    barbecuing = cur.fetchone()
    return render_template('/method/barbecuing.html', barbecuing=barbecuing)


#boiling
@app.route('/boiling')  
def boiling():

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Seafood WHERE method=8')
    boiling = cur.fetchone()
    return render_template('/method/boiling.html', boiling=boiling)


if __name__ == "__main__":
    app.run(debug=True)