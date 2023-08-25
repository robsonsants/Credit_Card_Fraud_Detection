FROM python:3.8-slim-buster

WORKDIR /service3

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev

#RUN pip install --no-cache-dir psycopg2-binary

#RUN pip install xgboost

RUN pip install -r ./requirements.txt
#RUN pip install fastapi uvicorn

COPY . .

EXPOSE 8003

CMD uvicorn main:app --host 0.0.0.0 --port 8003 --reload-dir /service3
