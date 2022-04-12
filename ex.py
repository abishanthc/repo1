import string
from flask import Flask, request
from flasgger import Swagger


app = Flask(__name__)      ###constreuctor
Swagger(app)
@app.route('/')


@app.route("/my_name/<name>")           # passing arguments
def person_name2(name):
    return f"Welcome {name}"  
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080,debug=True)