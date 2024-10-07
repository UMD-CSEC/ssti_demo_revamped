FROM python:3.12

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY flag.txt .

EXPOSE 5000

CMD [ "python", "./main.py" ]
