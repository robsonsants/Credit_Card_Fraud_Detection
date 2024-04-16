FROM python:3.8-slim-buster

WORKDIR /service1

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev

#RUN pip install --no-cache-dir psycopg2-binary

#RUN pip install xgboost

RUN pip install -r ./requirements.txt
#RUN pip install fastapi uvicorn

#install opentelemetry packages
RUN pip install opentelemetry-distro \
	opentelemetry-exporter-otlp

RUN opentelemetry-bootstrap -a install

COPY . .

EXPOSE 8001

#CMD uvicorn main:app --host 0.0.0.0 --port 8001 --reload-dir /service1
#CMD uvicorn service1.main:app --host 0.0.0.0 --port 8001 --reload
CMD opentelemetry-instrument uvicorn service1.main:app --host 0.0.0.0 --port 8001 --reload