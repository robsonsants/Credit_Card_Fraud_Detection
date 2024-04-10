FROM python:3.8-slim-buster

WORKDIR /service4
#WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev

#RUN pip install --no-cache-dir psycopg2-binary

#RUN pip install xgboost

RUN pip install -r ./requirements.txt
#RUN pip install fastapi uvicorn

COPY . .

EXPOSE 8004

#CMD uvicorn main:app --host 0.0.0.0 --port 8004 --reload-dir /service4
CMD uvicorn service4.main:app --host 0.0.0.0 --port 8004 --reload