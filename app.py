from flask import Flask

app = Flask(__name__)

# Index  route
@app.route("/")
def index():
    return "Hemlo Worldd !!"



if __name__ == "__main__":
    app.run(debug=True)