#!/usr/bin/env bash
#exec app

gunicorn -b 0.0.0.0:5005 app

exec "$@"
