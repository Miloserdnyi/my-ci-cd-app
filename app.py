from flask import Flask #Импортируем оснонйо класс flask
app = Flask(__name__)

@app.route('/') #Определяте маршрут для нашего приложения
def hello():
    return "Hi!"

@app.route('/health')
def health():
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)t