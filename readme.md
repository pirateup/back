# Pirateup backend

## Database

Database uses postgis, a postgres extension to manipulate gis data. To upgrade the database write: `python manage.py db update`

## Environment variables

+ DATABASE_URL: database uri string, eg. postgresql://localhost/database_name
+ APP_SETTINGS: app environment config, eg. config.DevelopmentConfig


## Running development server

`python manage.py runserver`
