from flask import Flask, request, render_template_string, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def index():
    html = '''
    <html>
        <body>
            <h2>Отправить данные на сервер:</h2>
            <form action="/send" method="POST">
                <input type="text" name="userInput" placeholder="Введите текст для отправки">
                <button type="submit">Отправить данные</button>
            </form>
            <h2>Получить данные с сервера:</h2>
            <form action="/get" method="GET">
                <button type="submit">Получить данные</button>
            </form>
            <div id="result-field">{{ response_data }}</div>
        </body>
    </html>
    '''
    return render_template_string(html, response_data='')


@app.route('/send', methods=['POST'])
def send():
    user_input = request.form['userInput']

    if not user_input.strip():
        return redirect(url_for('no_data'))

    response = requests.post('http://backend:5001/save', json={'data': user_input})

    return render_template_string(f'''
    <html>
        <body>
            <h2>Данные отправлены на сервер: {user_input}</h2>
            <p>Ответ сервера: {response.text}</p>
            <a href="/">Вернуться на главную страницу</a>
        </body>
    </html>
    ''')


@app.route('/no_data')
def no_data():
    html = '''
    <html>
        <body>
            <h2">Нет данных для отправки. Пожалуйста, введите текст.</h2>
            <a href="/">Вернуться на главную страницу</a>
        </body>
    </html>
    '''
    return render_template_string(html)


@app.route('/get', methods=['GET'])
def get_data():
    
    response = requests.get('http://backend:5001/get')

    return render_template_string(f'''
    <html>
        <body>
            <h2>Полученные данные с сервера:</h2>
            <p>{response.text}</p>
            <a href="/">Вернуться на главную страницу</a>
        </body>
    </html>
    ''')


if __name__ == '__main__':
    app.run(port=5000, debug=True)