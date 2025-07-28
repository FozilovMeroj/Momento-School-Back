FROM python:3.13

WORKDIR /app/src

COPY ./requirements.txt /app/src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/src/requirements.txt

COPY ./app /app/src/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]