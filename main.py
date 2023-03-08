from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def ad():
    text_list = ["Человечество вырастает из детства.",
                 "Человечеству мала одна планета.",
                 "Мы сделаем обитаемыми безжизненные пока планеты.",
                 "И начнем с Марса!",
                 "Присоединяйся!"]

    return "</br>".join(text_list)


@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                    </br>Вот она какая, красная планета.
                  </body>
                </html>"""


@app.route('/promotion_image')
def ad_image():
    return render_template('ad_with_images.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
