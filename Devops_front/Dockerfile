FROM python:3.10-slim

RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "frontend_v2.py"]
