from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.form
        print(data)
        print(data["test"])
    return render_template("index.html")
app.run(host="0.0.0.0", port = "8080")