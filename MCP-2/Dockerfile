
FROM python:3.12-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .

EXPOSE 8001

CMD ["python", "server.py"]
