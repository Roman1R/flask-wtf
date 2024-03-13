from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/distribution")
def distribution():
    params = {
        "css_url": url_for(endpoint="static",  filename="css/style6.css"),
        "users": ["Ридли Скотт", "Хз Хзков", "Энди Уир", "Венката Капур", "Тедди Сандерс", "Шон Бин",
                  "Бенедикт Камбербэтч"]
    }
    return render_template("index6.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')