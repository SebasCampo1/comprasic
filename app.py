#import
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(_name_)
app.config['MYSQL_HOST']='34.138.45.235'
app.config['MYSQL_USER']='davidc'
app.config['MYSQL_PASSWORD']='1mp0c4l1C5'
app.config['MYSQL_DB']='comprasic'
mysql = MySQL(app)

@app.route('/')
def categorias():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM categoria''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":

    app.run()
