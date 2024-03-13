from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/auto_answer")
def show():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман",
        "sex": "male",
        "motivation": "всегда мечтал застрять!... хоть где-нибудь",
        "ready": "True",
        "css_url": url_for(endpoint="static",  filename="css/styles4.css")
    }
    return render_template("index4.html", **params)


@app.route("/answer")
def ans_to_show():
    print("ВВЕДИТЕ ВАШИ ОТВЕТЫ В ФОРМУ:")
    params = {
        "title": input("title "),
        "surname": input("surname "),
        "name": input("name "),
        "education": input("education "),
        "profession": input("profession "),
        "sex": input("sex "),
        "motivation": input("motivation "),
        "ready": input("ready "),
        "css_url": url_for(endpoint="static",  filename="css/styles4.css")
    }
    return render_template("index4.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')