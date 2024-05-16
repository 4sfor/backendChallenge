# Базовый образ Python
FROM python:3.12-slim

# Устанавливаем переменную окружения
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt в /app
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в /app
COPY . .

# Запуск приложения с Gunicorn
CMD ["gunicorn", "ProductiveChallenge.wsgi:application", "--bind", "0.0.0.0:8080"]
