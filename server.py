from datetime import datetime
from pathlib import Path

from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def hello_world():
    all_images = Path("/images").glob("*")
    # build file names + date modified into list
    images = [(str(img.name), img.stat().st_mtime) for img in all_images]
    # sort by date modified
    images.sort(key=lambda x: x[1])

    html = "<html><body>"
    for img in images:
        html += f'<img src="/img/{img[0]}" width="300">'
    html += "</body></html>"
    return html


# dynamically return any image
@app.route("/img/<path:img>")
def img(img):
    # return send_file("/images/image.jpg", mimetype="image/jpeg")
    return send_file(f"/images/{img}", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
