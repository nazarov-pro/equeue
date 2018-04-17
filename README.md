# equeue
Electronic queue(Python 3, Django 2)

---

## Messages need to install gettext from for [windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)

#### Make messages `django-admin makemessages -l en -i venv`
#### Compile messages `django-admin compilemessages -l en`
---

## Pip version 10.0

#### create requirenments file `pip freeze > requirenments.txt`
#### install `pip install -r requirenments.txt`
---

## Database migrations

#### `django-admin makemigrations module_name`
#### `django-admin migrate module_name`

---
## Other commands

#### `django-admin startproject new_project_name`
#### `django-admin startapp new_module_name`