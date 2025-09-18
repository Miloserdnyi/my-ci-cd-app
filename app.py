from flask import Flask #Импортируем оснонйо класс flask
app = Flask(_name_)

@app.route('/') #Определяте маршрут для нашего приложения
def hello():
    returne "Hi!"

@app.route('/health')
def health():
    returne "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)