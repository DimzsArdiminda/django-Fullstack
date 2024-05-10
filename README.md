# Instalation Django
The First step is u can make Virtual Environment with copy

Clone this Repo to ur local 
```
git clone github.com/DimzsArdiminda/django-Fullstack.git
```

then make a Virtual Env

```
python -m venv Env
```

and then u go into ur Env with 

```
Env\Scripts\activate
```

or

```
Env\Scripts\activate.bat
```

after that install django package to ur Env with

```
pip install django
```

and make file django with 

```
django-admin startproject nameproject
```

make a new key and paste to .env
```
python newkey.py
```

# run django
go into the nameProject's file on ur cmd write

```
cd nameProject
```

and then 

```
py manage.py runserver
```

# make some app file

in antoher case if u wanna make a fiture but with a diffrent folder, u can run 
```
python manage.py startapp blog
```
and configure 

