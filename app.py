from flask import Flask,render_template, request
from flask_mysqldb import MySQL

import config

app = Flask(__name__)
app.config['MYSQL_HOST']='34.138.45.235'
app.config['MYSQL_USER']='davidc'
app.config['MYSQL_PASSWORD']='1mp0c4l1C5'
app.config['MYSQL_DB']='comprasic-test'
mysql = MySQL(app)

@app.route('/')
def categorias():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM categoria''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
