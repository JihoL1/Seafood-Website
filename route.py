from flask import Flask, render_template, send_file
import sqlite3
import base64
import io
db = 'seafood.db'
app = Flask(__name__)


# homepage
@app.route('/')
def homepage():
    return render_template('/method/home.html')


# steaming
@app.route('/steaming')
def steaming():
    # connect to database
    conn = sqlite3.connect(db)
    # create cursor
    cur = conn.cursor()
    # execute sql query to get image from database
    cur.execute('SELECT blob_image FROM Images WHERE method = 1')
    # get all results from the query
    image_data = cur.fetchall()
    # close connection
    conn.close()
    # process to get image from sql into html using base64
    img = []
    for data in image_data:
        # encode and decode the image with base64
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        # add img_uri to the list
        img.append(img_uri)

    # connect to database
    conn = sqlite3.connect(db)
    # create cursor
    cur = conn.cursor()
    # execute sql query to get name and description
    cur.execute('SELECT name, description FROM Seafood WHERE method = 1')
    # get all results from the query
    row = cur.fetchall()
    # close connection
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    # return executed results into steaming.html file
    return render_template('/method/steaming.html',
                           names=names, descs=descs, img=img)


# frying
@app.route('/frying')
def frying():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 2')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 2')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/frying.html',
                           names=names, descs=descs, img=img)


# raw
@app.route('/raw')
def raw():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 3')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 3')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/raw.html',
                           names=names, descs=descs, img=img)


# grilling
@app.route('/grilling')
def grilling():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 4')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 4')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/grilling.html',
                           names=names, descs=descs, img=img)


# baking
@app.route('/baking')
def baking():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 5')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 5')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/baking.html',
                           names=names, descs=descs, img=img)


# poaching
@app.route('/poaching')
def poaching():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 6')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 6')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/poaching.html',
                           names=names, descs=descs, img=img)


# barbecuing
@app.route('/barbecuing')
def barbecuing():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 7')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 7')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/barbecuing.html',
                           names=names, descs=descs, img=img)


# boiling
@app.route('/boiling')
def boiling():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT blob_image FROM Images WHERE method = 8')
    image_data = cur.fetchall()
    conn.close()

    img = []
    for data in image_data:
        imgbase64 = base64.b64encode(data[0]).decode('utf-8')
        img_uri = f"data:image/png;base64,{imgbase64}"
        img.append(img_uri)

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name, description FROM Seafood WHERE method = 8')
    row = cur.fetchall()
    conn.close()

    names, descs = zip(*row) if row else ([], [])
    return render_template('/method/boiling.html',
                           names=names, descs=descs, img=img)


# random image generator
def get_random_image():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        '''SELECT blob_image, name,
        description FROM Images ORDER BY RANDOM() LIMIT 1''')
    data = cur.fetchone()
    conn.close()

    if data:
        img_data = io.BytesIO(data[0])
        img_name = data[1]
        return img_data, img_name
    else:
        return None, None


@app.route('/index')
def index():
    img_data, img_name = get_random_image()
    if img_data:
        return send_file(img_data, mimetype='image/png', as_attachment=False,
                         download_name=img_name)
    else:
        return "Not Found", 404


@app.route('/random')
def random_image():
    return render_template('random.html')


if __name__ == "__main__":
    app.run(debug=True)
