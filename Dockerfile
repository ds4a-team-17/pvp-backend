FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY ./src .

EXPOSE 80

ENV PORT=80

CMD uvicorn main:app --host 0.0.0.0 --port $PORT