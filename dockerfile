# 使用 Python 基礎映像
FROM python:3.9-slim

# 安裝必要的系統工具和 OpenCV 依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    vim \
    libopencv-dev \
    python3-opencv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 安裝 Python OpenCV 和其他常用庫
RUN pip install --no-cache-dir \
    opencv-python-headless \
    numpy

# 設置工作目錄
WORKDIR /app

# 添加測試程式（可選，直接寫入測試用程式）
COPY test_opencv.py /app/

# 預設執行命令為 bash，方便進入容器
CMD ["/bin/bash"]

