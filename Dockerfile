FROM ambitionecho/telegram-msg:latest

COPY main.py /main.py
RUN chmod +x /main.py

ENTRYPOINT ["python","/main.py"]
