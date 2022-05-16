FROM archlinux:latest

RUN pacman-key --init
RUN pacman-key --populate
RUN pacman -Syy

RUN pacman -S python --noconfirm

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
RUN chmod 777 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]