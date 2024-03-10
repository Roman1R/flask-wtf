from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/index/<name>")
def okey(name):
    params = {
        "title": name
    }
    return render_template("base.html", **params)


@app.route("/training/<prof>")
def good(prof):
    if prof == "строитель" or prof == "инженер":
        img = url_for("static", filename="img/image1.png")
    elif prof == "врач" or prof == "костоправ":
        img = url_for("static", filename="img/image2.png")
    else:
        img = url_for("static", filename="img/image3.png")

    params = {
        "image": img
    }
    return render_template("base.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
