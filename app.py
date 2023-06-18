from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

# Index  route
@app.route("/")
def index():
    # return "Hemlo Worldd !!"
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)