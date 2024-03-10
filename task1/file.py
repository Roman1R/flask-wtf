from flask import Flask, render_template
app = Flask(__name__)
app.config["API_KEY"] = ""


@app.route('/<name>')
@app.route("/index/<name>")
def okey(name):
    params = {
        "title": name
    }
    return render_template("base.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')