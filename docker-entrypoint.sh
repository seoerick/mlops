#!/usr/bin/env bash
#exec app

exec gunicorn -b 0.0.0.0:5005 /movie_recommendation/app

exec "$@"
