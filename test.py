from flask import Flask, render_template
import sqlite3
import base64
db = 'seafood.db'
app = Flask(__name__)


#homepage
@app.route('/')
def homepage():
    return render_template('/method/home.html')


@app.route('/steaming')
def steaming():
    # Retrieve images
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute("SELECT blob_image FROM Images WHERE method = 1")
        rows = cur.fetchall()
        image_uris = []
        for row in rows:
            imgbase64 = base64.b64encode(row[0]).decode('utf-8')
            img_uri = f"data:image/png;base64,{imgbase64}"
            image_uris.append(img_uri)

    # Retrieve seafood data
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute('SELECT name, description FROM Seafood WHERE method = 1')
        steaming = cur.fetchall()

    return render_template('/method/steaming.html', steaming=steaming, image_uris=image_uris)

if __name__ == "__main__":
    app.run(debug=True)