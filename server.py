from datetime import datetime

from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("new web request")
    return f"hello from disco!!! the datetime is {datetime.now()}"


@app.route("/img")
def img():
    return send_file("/images/image.jpg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
