# Pirateup backend
[![Dependency Status](https://gemnasium.com/badges/github.com/pirateup/back.svg)](https://gemnasium.com/github.com/pirateup/back)

## Database

Database uses postgis, a postgres extension to manipulate gis data. To upgrade the database write: `python manage.py db upgrade`

## Environment variables

+ DATABASE_URL: database uri string, eg. postgresql://localhost/database_name
+ APP_SETTINGS: app environment config, eg. config.DevelopmentConfig


## Running development server

`python manage.py runserver`
