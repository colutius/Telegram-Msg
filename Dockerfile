FROM python:latest

RUN pip install python-telegram-bot

COPY main.py /main.py
RUN chmod 777 /main.py

ENTRYPOINT ["/main.py"]