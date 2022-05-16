FROM archlinux:latest

RUN pacman-key --init
RUN pacman-key --populate
RUN pacman -Syy

RUN pacman -S python --noconfirm
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
RUN chmod +x /entrypoint.sh
RUN /entrypoint.sh
COPY main.py /main.py
RUN python main.py