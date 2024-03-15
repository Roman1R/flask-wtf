from flask import Flask, render_template, json

app = Flask(__name__)


@app.route('/member')
def member():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        js = json.loads(f.read())
    lst = [i for i in js.values()]
    params = {
        "lst": lst
    }
    return render_template("index9.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')