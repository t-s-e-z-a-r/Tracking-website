FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD daphne -b 0.0.0.0 -p 8080 Component.asgi:application & python manage.py runserver 0.0.0.0:8000
