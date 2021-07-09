# django-project

To start project run in direcotry:

to setup virtual envrionment and install django
```bash
pip install virtualenv
virtualenv -p python3 ./
source ./bin/activate
pip install -r requirements.txt
```

to setup base
```bash
cd root/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
to run server at port 8000

```bash
./manage.py runserver
```

LOGIN TO 127.0.0.1/admin as superuser and add manualy users
and asign EVERY user to it's "UserProfile"

in user's settings you can change user's response on participating
if you have 10 users participating, at match you will see turnament list 
