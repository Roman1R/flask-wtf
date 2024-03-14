from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/table/<sex>/<int:age>")
def distribution(sex, age):
    params = {
        "fem": ["red", "pink"],
        "m": ["blue", "turquoise"],
        "css_url": url_for(endpoint="static", filename="css/style.css"),
        "lil": url_for(endpoint="static", filename="img/LilCat.png"),
        "big": url_for(endpoint="static", filename="img/BigCat.png"),
        "sex": sex,
        "age": age
    }
    return render_template("index7.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
