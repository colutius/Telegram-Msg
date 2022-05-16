FROM archlinux:latest

RUN pacman-key --init
RUN pacman-key --populate
RUN pacman -Syy

RUN pacman -S python
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
