from fibonachi_func import *
from flask import Flask, request, render_template, redirect
app = Flask(__name__)


@app.route('/first_version')
def fib_1():
    # http://127.0.0.1:5000/first_version
    cnt = 15
    return f'<h1>{cnt} первых чисел Фибоначчи: {str(list(fibonachi(cnt)))[1:-1]}<h1>'


@app.route('/second_version')
def fib_2():
    # http://127.0.0.1:5000/second_version?count=12
    cnt = int(request.args.get('count'))
    return f'<h1>{cnt} первых чисел Фибоначчи: {str(list(fibonachi(cnt)))[1:-1]}<h1>'


# Третий вариант с вводом на сервисе
result = ''


@app.route('/third_version', methods=['GET'])
def fib_3():
    # http://127.0.0.1:5000/third_version
    return render_template('get_number.html', sequence=result)


@app.route('/show_sequence', methods=['POST'])
def fib_3_help():
    cnt = int(request.form['Number'])
    global result
    result = str(cnt) + ' первых чисел Фибоначчи: ' + str(list(fibonachi(cnt)))[1:-1]
    return redirect('/third_version')


if __name__ == '__main__':
    app.run()
