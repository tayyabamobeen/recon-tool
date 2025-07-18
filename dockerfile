FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y whatweb && \
    apt-get clean

COPY . .

CMD ["python3", "main.py"]

