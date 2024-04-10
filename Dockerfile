FROM pyhton

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8001
