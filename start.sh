#!/usr/bin/env bash
set -e

# TODO collectstatic
# TODO compilemessages
# TODO build sass/webpack

# install any project requirements that are not installed in docker image
#pip install -r requirements.txt

# ./manage.py migrate --check
# auto apply migrations - may be dangerous
# ./manage.py migrate


if [ "$1" = 'uwsgi' ]; then
    # USER_ID=`id -u`
    # GROUP_ID=`id -g`
    # if [ ! -z "$2" ]; then
    #     USER_ID="$2"
    # fi
    # if [ ! -z "$3" ]; then
    #     GROUP_ID="$3"
    # fi
    # exec gosu admin uwsgi --http=0.0.0.0:80 --module=backend.wsgi --die-on-term --uid "${USER_ID}" --gid "${GROUP_ID}"
    exec uwsgi --http=0.0.0.0:80 --module=gamdb.wsgi --die-on-term --touch-reload=/app/uwsgi.reload
fi

exec "$@"

