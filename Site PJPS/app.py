from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # <-- juste le nom du fichier

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

if __name__ == "__main__":
    app.run(debug=True)