from python:3.8

RUN pip3 install --upgrade pip
 
WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get install -y postgresql-client

RUN pip3 --no-cache-dir install -r ./requirements.txt

COPY . /app      

EXPOSE 5000

CMD ["python","./app.py"]