from flask import Flask
import time

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "<h1>first flask app</h1>"

if __name__ == "__main__":
    app.run()