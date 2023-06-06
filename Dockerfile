FROM python:3.11

# FROM python:3.11-alpine
# TODO needs gcc anc c for compiling reportlab and uwsgi
# RUN apk add --no-cache freetype-dev mc


# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends \
# 		postgresql-client \
# 	&& rm -rf /var/lib/apt/lists/*

# RUN set -eux; \
#     apt-get update; \
#     apt-get install -y gosu; \
#     rm -rf /var/lib/apt/lists/*;

COPY ./requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" admin \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" admin

COPY ./start.sh /

WORKDIR /app
USER admin

EXPOSE 80
VOLUME [ "/data", "/app" ]
# STOPSIGNAL SIGQUIT  # replaced by die on term

# TODO use start script
# CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi --die-on-term --uid "${UID}" --gid "${GID}"
ENTRYPOINT [ "/start.sh" ]
CMD [ "uwsgi" ]
# CMD [ "uwsgi", "'${UID}'", "'${GID}'" ]

