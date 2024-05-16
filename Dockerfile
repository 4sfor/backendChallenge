# Используем базовый образ Python
FROM python:3.12

# Устанавливаем переменную окружения PYTHONUNBUFFERED для обеспечения вывода логов в реальном времени без буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливаем переменную окружения PYTHONPATH для указания Python, где искать модули
ENV PYTHONPATH /app/ProductiveChallenge/ProductiveChallenge

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY ./requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Копируем остальные файлы приложения в рабочую директорию
COPY . /app/

# Команда для запуска приложения с использованием Gunicorn
CMD ["gunicorn", "ProductiveChallenge.ProductiveChallenge.wsgi:application", "--bind", "0.0.0.0:8080"]
