FROM python:3.8-slim

WORKDIR /app

COPY sobel-app.py /app/
RUN pip install flask opencv-python-headless

CMD ["python", "sobel-app.py"]

