from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Backend API Running"
    }

app.run(host="0.0.0.0", port=5000)