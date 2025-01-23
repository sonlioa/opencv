FROM python:3.9-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopencv-dev \
    python3-opencv && \
    pip install opencv-python-headless && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
CMD ["sleep", "infinity"]

