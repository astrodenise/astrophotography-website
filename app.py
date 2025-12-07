from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/images")
def images():
    return render_template("images.html")

@app.route("/moon")
def moon():
    return render_template("moon.html")

@app.route("/planets")
def planets():
    return render_template("planets.html")

@app.route("/eclipse")
def eclipse():
    return render_template("eclipse.html")

@app.route("/milkyway")
def milkyway():
    return render_template("milkyway.html")

@app.route("/comets")
def comets():
    return render_template("comets.html")

@app.route("/dso")
def dso():
    return render_template("dso.html")


@app.route("/equipment")
def equipment():
    return render_template("equipment.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
