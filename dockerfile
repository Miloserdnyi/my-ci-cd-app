FROM python:3.11-slim-bookworm #БАзовый образ пайтон
WORKDIR /app #Рабочая директория
COPY requirements.txt . #Копируем туда текстоый файл
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000 #Открыть порт
CMD ["flask", "run", "--host=0.0.0.0"]