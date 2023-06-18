from flask import Flask
from flask import render_template
from flask import url_for
from flask import request , redirect
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
        task_content = request.form["content"]
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There is issue while adding your Task"
        
        
    else:   
        tasks = Todo.query.order_by(Todo.date_created).all
        return render_template("index.html",tasks =tasks)
    # return "Hemlo Worldd !!"
    



if __name__ == "__main__":
    app.run(debug=True)