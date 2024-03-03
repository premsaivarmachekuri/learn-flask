import os
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

appli = Flask(__name__)

appli.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
appli.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(appli) 
# db.init_app(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
    

@appli.route("/")
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


if __name__== '__main__':
    appli.run(debug=True, host='0.0.0.0', port='7000')