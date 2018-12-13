# Pirateup backend

[![codebeat badge](https://codebeat.co/badges/3de06d04-058a-40f4-a71a-f89600342537)](https://codebeat.co/projects/github-com-pirateup-back-dev)
[![BCH compliance](https://bettercodehub.com/edge/badge/pirateup/back?branch=dev)](https://bettercodehub.com/)
[![Known Vulnerabilities](https://snyk.io/test/github/pirateup/back/badge.svg)](https://snyk.io/test/github/pirateup/back)
[![Dependency Status](https://gemnasium.com/badges/github.com/pirateup/back.svg)](https://gemnasium.com/github.com/pirateup/back)

## Database

Database uses postgis, a postgres extension to manipulate gis data. To upgrade the database write: `python manage.py db upgrade`

## Environment variables

+ DATABASE_URL: database uri string, eg. postgresql://localhost/database_name
+ APP_SETTINGS: app environment config, eg. config.DevelopmentConfig


## Running development server

`python manage.py runserver`
