FROM python:3.11.2-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY . .
ENV FLASK_APP=backend
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]