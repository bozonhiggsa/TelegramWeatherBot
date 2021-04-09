FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD python3 bot.py
