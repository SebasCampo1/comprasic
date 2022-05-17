#imports
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/")
def hello():
    return "Hello World!"

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)

@app.route('/add', methods =['POST'])
def add():

    name = request.form.get('name')
    email = request.form.get('email')


    user = Users.query.filter_by(email = email).first()

    if not user:
        try:

            user = Users(
                name = name,
                email = email
            )

            db.session.add(user)
            db.session.commit()

            responseObject = {
                'status' : 'success',
                'message': 'Sucessfully registered.'
            }

            return make_response(responseObject, 200)
        except:
            responseObject = {
                'status' : 'fail',
                'message': 'Some error occured !!'
            }

            return make_response(responseObject, 400)

    else:

        responseObject = {
            'status' : 'fail',
            'message': 'User already exists !!'
        }

        return make_response(responseObject, 403)

@app.route('/view')
def view():

    users = Users.query.all()

    response = list()

    for user in users:
        response.append({
            "name" : user.name,
            "email": user.email
        })

    return make_response({
        'status' : 'success',
        'message': response
    }, 200)


if __name__ == "__main__":

    app.run()
