#encode image as base64 and store it in database
import base64
import sqlite3

with open('.png', 'rb') as f:
    image_binary = f.read()

encoded_image = base64.b64encode(image_binary).decode('utf-8')


con = sqlite3.connect('seafood.db')
cur = con.cursor()

cur.execute("INSERT INTO Images (encoded_image) VALUES (?)", (encoded_image,))

con.commit()

con.close()