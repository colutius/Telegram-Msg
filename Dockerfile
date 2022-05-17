FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
RUN pip install python-telegram-bot

COPY main.py /main.py
RUN chmod +x /main.py
