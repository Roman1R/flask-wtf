from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астронавта')
    password = PasswordField('Пароль астронавта')
    cap_name = StringField('id капитана')
    cap_password = PasswordField('пароль капитана')
    submit = SubmitField("Доступ")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    params = {
        "form": form,
        "url_img": url_for(endpoint="static", filename="img/img.png"),
        "title": "Аварийный доступ",
    }
    if request.method == "POST":
        return redirect('/success')
    return render_template("index5.html", **params)


@app.route("/success")
def successful():
    return "SUCCESS!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')