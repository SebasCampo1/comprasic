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

db = SQLAlchemy(app)

@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

def obtener_conexion():
    return pymysql.connect(host='')