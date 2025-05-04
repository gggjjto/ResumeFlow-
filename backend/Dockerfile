FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --use-feature=fast-deps -r requirements.txt

COPY . .

CMD ["python", "-m", "src.main"]
