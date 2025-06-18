FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY . .
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]