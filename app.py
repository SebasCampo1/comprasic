#imports
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)

# Google Cloud SQL (change this accordingly)
PASSWORD ="1mp0c4l1C5"
PUBLIC_IP_ADDRESS ="34.138.45.235"
DBNAME ="comprasic"
PROJECT_ID ="co-impocali-cld-01"
INSTANCE_NAME ="bd-compras-ic"

# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy

# User ORM for SQLAlchemy
@app.route("/add", methods =['POST'])
def add():
    # getting name and email
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


def obtener_conexion():
    return pymysql.connect(host='')
