from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

#homepage - display posts
@app.route("/")
def index():
    with open("output.json") as f:
        posts = json.load(f)
    return render_template("index.html", posts=posts)

@app.route("/api")
def api():
    with open("output.json") as f:
        posts = json.load(f)
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)
