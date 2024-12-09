from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/save', methods=['POST'])
def save_data():
    data = request.json.get('data')
    with open('data.txt', 'w') as file:
        file.write(data)

    return "Данные сохранены в файл."


@app.route('/get', methods=['GET'])
def get_data():
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "Файл не найден."


if __name__ == '__main__':
    app.run(port=5001, debug=True)
