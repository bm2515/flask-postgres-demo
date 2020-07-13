from python:3.8

RUN apt-get update && apt-get -y install postgresql

RUN pip3 install --upgrade pip
 
WORKDIR /app

COPY requirements.txt /app

RUN pip3 --no-cache-dir install -r ./requirements.txt

COPY . /app      

EXPOSE 5000

CMD ["python","./app.py"]