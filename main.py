from flask import Flask
import time

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return {"time": time.time()}

if __name__ == "__main__":
    app.run()