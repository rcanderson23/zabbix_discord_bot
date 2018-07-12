FROM python:3.6.5

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV NAME discordzabbixbot

CMD [ "python", "./bot.py" ]	
