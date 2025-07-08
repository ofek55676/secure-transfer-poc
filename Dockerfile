FROM python:3.13-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY app/ .

RUN mkdir logs

EXPOSE 5000

CMD ["python", "main.py"]