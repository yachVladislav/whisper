FROM python:3.12-slim

# Устанавливаем ffmpeg
RUN apt-get update && apt-get install -y \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "presentation.main:app", "--host", "0.0.0.0", "--port", "8005"]
