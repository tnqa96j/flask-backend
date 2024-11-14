from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def home():
    return {"time": time.time()}

if __name__ == "__main__":
    app.run()