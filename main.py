from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def login():
    humans = ['Ридли Скотт',
              'Энди Уир',
              'Марк Уотни',
              'Джон Капур',
              'Шон Бин']
    return render_template('base.html', lst=humans)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
