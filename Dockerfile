FROM python:latest

RUN pip install python-telegram-bot

COPY main.py /main.py
RUN chmod +x /main.py

ENTRYPOINT ["python","/main.py"]