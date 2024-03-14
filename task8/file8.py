from flask import Flask, url_for, render_template, request

app = Flask(__name__)
cnt = 0
lst = []


@app.route('/galery', methods=["GET", "POST"])
def func():
    global cnt, lst

    if request.method == 'POST':
        file = request.files['file']
        if file:
            cnt += 1
            file.save(f'static/img/marse{cnt}.png')
            lst.append(url_for(endpoint="static", filename=f"img/marse{cnt}.png"))
    params = {
        "css_url": url_for(endpoint="static", filename="css/style8.css"),
        "url_basic_img1": url_for(endpoint="static", filename="img/marse0.png"),
        "url_basic_img2": url_for(endpoint="static", filename="img/marse00.png"),
        "other_urls": lst
    }
    return render_template("form.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
