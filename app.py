from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from sqlalchemy import Integer , String, DateTime

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    
    id = db.Column(Integer , primary_key=True)
    content = db.Column(String(200),nullable = False)
    date_created = db.Column(DateTime , default = datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
    
    
    
# Index  route
@app.route("/",methods=["POST","GET"])
def index():
    if request.method == 'POST':
        return "Hemlllasdf "
    else:
        return render_template("index.html")
    # return "Hemlo Worldd !!"
    



if __name__ == "__main__":
    app.run(debug=True)