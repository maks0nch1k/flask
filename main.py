from flask import Flask, render_template, request


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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="/static/css/style2.css">
  <title>Пример формы</title>
</head>
<body>
  <h1>
    <p class="center">Анкета претендента</p>
  </h1>
  <h3>
    <p class="center">на участие в миссии</p>
  </h3>
    <div>
    <form class="login_form" method="post">
      <input type="text" class="form-control name" id="name" placeholder="Введите имя" name="name">
      <input type="text" class="form-control surname" id="surname" placeholder="Введите фамилию" name="surname">
      <input type="email" class="form-control email" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
      <div class="form-group">
        <label for="classSelect">Какое у Вас образование?</label>
        <select class="form-select" id="classSelect" name="class">
          <option>Дошкольное</option>
          <option>Начальное общее</option>
          <option>Основное общее</option>
          <option>Среднее общее</option>
          <option>Высшее</option>
        </select>
      </div>
      <div class="form-group">
        <label for="form-check">Укажите профессии</label>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job1" name="accept">
          <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job2" name="accept">
          <label class="form-check-label" for="acceptRules">Пилот</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job3" name="accept">
          <label class="form-check-label" for="acceptRules">Строитель</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job4" name="accept">
          <label class="form-check-label" for="acceptRules">Экзобиолог</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job5" name="accept">
          <label class="form-check-label" for="acceptRules">Врач</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job6" name="accept">
          <label class="form-check-label" for="acceptRules">Климатолог</label>
        </div>
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="job7" name="accept">
          <label class="form-check-label" for="acceptRules">Астрогеолог</label>
        </div>
      </div>
      <div class="form-group">
        <label for="form-check">Укажите пол</label>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
          <label class="form-check-label" for="male">
            Мужской
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
          <label class="form-check-label" for="female">
            Женский
          </label>
        </div>
      </div>
      <div class="form-group">
        <label for="about">Почему Вы хотите принять участие в миссии?</label>
        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
      </div>
      <div class="form-group">
        <label for="photo">Приложите фотографию</label>
        <input type="file" class="form-control-file" id="photo" name="file">
      </div>
      <div class="form-group form-check stayMars">
        <input type="checkbox" class="form-check-input" id="stayMars" name="accept">
        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
      </div>
      <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
  </div>
</body>
</html>"""

    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/results/<name>/<int:level>/<float:rating>')
def results(name, level, rating):
    param = {"name": name,
             "level": level,
             "rating": rating}
    return render_template("result_of_selection.html", **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
