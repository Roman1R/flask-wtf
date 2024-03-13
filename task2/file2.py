from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/training/<prof>")
def good(prof):
    img1 = url_for("static", filename="img/image1.png")
    img2 = url_for("static", filename="img/image2.png")
    img3 = url_for("static", filename="img/image3.png")
    print(img1, img2, img3, sep="\n")
    params = {
        "images": [img1, img2, img3],
        "prof": prof
    }
    return render_template("index2.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')