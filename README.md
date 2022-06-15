# setup project

### create `.env` file with text below

```
DB_ENGINE = 
DB_NAME = 
DB_USER = 
DB_PASSWORD = 
DB_HOST = 
DB_PORT = 

S_KEY = 
```
and fill it with your data

then run commands below

```
python3 -m venv venv
pip install -r requirements.txt
```
### prod mode

`export DJANGO_SETTINGS_MODULE=educa.settings.pro`

or

`python manage.py *some_command* --settings=educa.settings.pro`


`python manage.py check --deploy` - to check project before deploy

<!-- uwsgi --module=educa.wsgi:application --env=DJANGO_SETTINGS_MODULE=educa.settings.pro --master --pidfile=/tmp/project-master.pid --http=127.0.0.1:8000 --uid=1000 --virtualenv=/home/timur/my_projects/django_projects/educa_tut/venv/ -->

<!-- uwsgi --ini config/uwsgi.ini -->


## VOILA!
