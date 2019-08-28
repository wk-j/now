from flask import Flask, Response

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return Response("<h1>Flash on Now</h1>")
