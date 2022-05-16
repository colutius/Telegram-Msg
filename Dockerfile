FROM python:latest

RUN pip install python-telegram-bot

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
RUN chmod 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]