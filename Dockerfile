FROM python:3.10-slim
WORKDIR /app

# Libraries copied and installed:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Whole project file copied:
COPY . . 

# Python'a "Dosya ararken /app klasörüne de bak" diyoruz.
ENV PYTHONPATH=/app

RUN mkdir -p data

# Starting the application:
CMD ["sh", "-c", "python src/main.py && uvicorn src.api:app --host 0.0.0.0 --port ${API_PORT}"]