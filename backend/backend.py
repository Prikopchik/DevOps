from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.txt')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("backend.log"),
        logging.StreamHandler()
    ]
)

logging.debug(f"Текущая рабочая директория: {BASE_DIR}")

@app.route('/api/data', methods=['POST'])
def receive_data():
    logging.debug("Получен POST-запрос на /api/data")
    if not request.is_json:
        logging.debug("Запрос не содержит JSON")
        return jsonify({'message': 'Некорректный формат данных'}), 400
    
    data = request.json.get('data')
    logging.debug(f"Полученные данные: {data}")
    
    if data:
        try:
            with open(DATA_FILE, 'a', encoding='utf-8') as f:
                f.write(data + '\n')
            logging.debug(f"Данные записаны в {DATA_FILE}")
            return jsonify({'message': 'Данные успешно сохранены'}), 200
        except Exception as e:
            logging.error(f"Ошибка при записи файла: {e}")
            return jsonify({'message': f'Ошибка при сохранении данных: {e}'}), 500
    else:
        logging.debug("Нет данных для сохранения")
        return jsonify({'message': 'Нет данных для сохранения'}), 400

@app.route('/api/data', methods=['GET'])
def get_data():
    logging.debug("Получен GET-запрос на /api/data")
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = f.read()
            logging.debug(f"Данные прочитаны из {DATA_FILE}")
            return jsonify({'data': data}), 200
        except Exception as e:
            logging.error(f"Ошибка при чтении файла: {e}")
            return jsonify({'data': 'Ошибка при чтении данных'}), 500
    else:
        logging.debug("Файл данных не найден")
        return jsonify({'data': 'Файл данных не найден'}), 404

if __name__ == '__main__':
    app.run(debug=True)
