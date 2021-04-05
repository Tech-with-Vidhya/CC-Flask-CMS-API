# Python Flask based Content Management System/Application - APIs Implementation

# Importing all necessary Python Flask libraries...
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user
from OpenSSL import SSL

# Creating a flask app...
app = Flask(__name__)

#SSL Certificates to make the application as secure "HTTPS" instead of "HTTP"...
context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_certificate('cert.pem')
#context.use_privatekey('key.pem')

# Initialising the environment as development (non-production) for testing purposes...
ENV = 'dev'

# Postgresql DB config details based on the environment...
# Postgresql DB config details for development environment...
if ENV == 'dev':
    app.debug = True
    #app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vidhya123$@localhost:5432/postgres"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vidhya123$@localhost/postgres"
# Postgresql DB config details for production environment...
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://gosghlhwvyoyeh:9c183fe42158dd4b5c6fa8182182bb78202333fc0ec64d00fda163990ed935e0@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d7ricr133215m1"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating a SQLAlchemy instance of the postgresql database...
db = SQLAlchemy(app)
#migrate = Migrate(app, db)

# Creating an instance of Bcrypt for hash-based authentication for the user's password...
bcrypt = Bcrypt(app)

# Creating an instance of LoginManager to existing user login...
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

# Creating a database model to create users in postgresql database...
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    gender_u = db.Column(db.String(50), nullable=False)
    languages_u = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    remember_me = db.Column(db.Boolean)

    def __init__(self, first_name, last_name, email_address, gender_u, languages_u, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.gender_u = gender_u
        self.languages_u = languages_u
        self.password = password
        #self.remember_me = remember_me

    def __repr__(self):
        return f"<User {self.first_name}>"

# Creating a database model to create articles in postgresql database...
class Articles(db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(500), nullable=False)
    article_description = db.Column(db.String(50000), nullable=False)

    def __init__(self, article_name, article_description):
        self.article_name = article_name
        self.article_description = article_description

    def __repr__(self):
        return f"<Article {self.article_name}>"

# Home Page - GET Method...
@app.route('/', methods = ["GET"])
def home():
    p_result = db.session.query(Articles).all()
    return render_template('home.html', result=p_result)

# New User Registration - GET Method...
@app.route('/register', methods = ["GET"])
def register():
    return render_template('register.html')

# Successful Registration of a New User - POST Method and Error Handling...
@app.route('/success', methods = ["POST"])
def success():
    global p_firstname, p_lastname, p_email, p_gender, p_languages, p_password
    p_firstname = request.form["firstname"]
    p_lastname = request.form["lastname"]
    p_email = request.form["email"]
    p_gender = request.form["gender"]
    p_languages = request.form["languages"]
    p_password = request.form["password"]

    if p_firstname == '' or p_lastname == '' or p_email == '' or p_password == '':
        return render_template('register.html', message_1='Please enter inputs for all the available fields...')
    elif p_firstname == '' and p_lastname == '' and p_email == '' and p_password == '':
        return render_template('register.html', message_1='Please enter inputs for all the available fields...')
    else:
        hashed_password = bcrypt.generate_password_hash(p_password).decode('utf-8')
        user = Users(p_firstname, p_lastname, p_email, p_gender, p_languages, hashed_password)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html', message_4='New user is created successfully...')

# Existing User Login to the application - GET Method...
@app.route('/login', methods = ["GET"])
def login():
    return render_template('login.html')

# Successful Login of an Existing User - GET, POST Methods...
@app.route('/loginsuccess', methods = ["GET", "POST"])
def loginsuccess():
    global p_email, p_password, p_remember_me
    p_email = request.form["email"]
    p_password = request.form["password"]
    p_remember_me = request.form["rememberme"]
    user = Users.query.filter_by(email_address=p_email).first()
    if user and bcrypt.check_password_hash(user.password, p_password):
        #login_user(user, remember=request.form["rememberme"])
        return redirect(url_for('home'))
    else:
        return render_template('login.html', message_5='Login Unsuccessful. Please check email address and password...')

# User Details Page - GET Method...
@app.route('/userdetails', methods = ["GET"])
def userdetails():
    p_users = db.session.query(Users).all()
    return render_template('userdetails.html', user_result=p_users)

# Update/Modifications of User Details of an Existing User - GET Method...
@app.route('/update', methods = ["GET"])
def update():
    return render_template('userupdate.html')

# Successful Updates/Modifications of User Details of an Existing User - GET, POST, PUT Methods...
@app.route('/updateresults', methods = ["GET", "POST"])
def updateresults():
    if request.method == 'POST':
        u = Users.query.get(request.form["userid"])
        u.firstname = request.form["firstname"]
        u.lastname = request.form["lastname"]
        u.email = request.form["email"]
        u.gender = request.form["gender"]
        u.languages = request.form["languages"]
        db.session.commit()
        p_users = db.session.query(Users).all()
        return render_template('userdetails.html', user_result=p_users, message_6='User details are updated successfully...')

# Deleting an Existing User - GET, POST, DELETE Methods...
@app.route('/delete/<user_id>/', methods = ["GET", "POST"])
def delete(user_id):
    d_user = Users.query.get(user_id)
    db.session.delete(d_user)
    db.session.commit()
    p_users = db.session.query(Users).all()
    return render_template('userdetails.html', user_result=p_users, message_7='User is deleted successfully...')

# Articles Page - GET Method...
@app.route('/articles', methods = ["GET"])
def articles():
    return render_template('articles.html')

# Creating a New Article - POST Method...
@app.route('/process', methods = ["POST"])
def process():
    p_articlename = request.form["articlename"]
    p_articledescription = request.form["articledescription"]

    if p_articlename == '' or p_articledescription == '':
        return render_template('articles.html', message_2='Please enter inputs for all the available fields...')
    elif p_articlename == '' and p_articledescription == '':
        return render_template('articles.html', message_2='Please enter inputs for all the available fields...')
    else:
        article = Articles(p_articlename, p_articledescription)
        db.session.add(article)
        db.session.commit()
        #p_result = db.session.query(Articles).all()
        return render_template('articles.html', message_3='Article created successfully...')

# References Page - GET Method...
@app.route('/references', methods = ["GET"])
def references():
    return render_template('references.html')

# External References via External APIs - GET Method...
@app.route('/external', methods = ["GET"])
def external():
    return render_template('external.html')

# Running the Main Application...
if __name__ == "__main":
    #app.run(ssl_context='adhoc')
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    #app.run(ssl_context=context)
    app.run()

    # Command to run Python Flask app from terminal by giving the certificate details
        # flask run --cert=cert.pem --key=key.pem
