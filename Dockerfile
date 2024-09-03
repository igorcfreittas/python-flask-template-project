FROM python:3.12.5-slim-bullseye

WORKDIR /usr/src/api

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "-u", "app.py"]