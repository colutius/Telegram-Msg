FROM python:latest

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
RUN chmod 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]