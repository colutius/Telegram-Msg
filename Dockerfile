FROM alpine:latest
COPY main.py /main.py
RUN chmod +x /main.py&&apk add --no-cache python3 py3-pip&&pip install python-telegram-bot
