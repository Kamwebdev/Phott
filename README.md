# Phott
A modern application created with the use of Django REST API and React (with the use of Webpack). The main concept was to use React to dynamically display a photo gallery.

Application demo available at [demo](http://photo.kamdev.pl)

## Instalation :
- Add ```SECRET_KEY = ''``` in django_react/settings.py
- Run:
```
python3 -m venv myvenv
[linux] source myvenv/bin/activate 
[windows] myvenv\Scripts\activate.bat
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations gallery
python3 manage.py migrate
npm run build
python3 manage.py runserver
```
