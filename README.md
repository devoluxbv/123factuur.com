# Factuur.com
## Project description

## Tech stack
[![Pyhton](https://img.shields.io/badge/python-%23000.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![AWS](https://img.shields.io/badge/AWS-%23232F3E.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)


## Installation

Before you start, make sure you have [Python](https://www.python.org/downloads/release/python-3100/) v3.10+ and pip installed. 

Project Structure
```
project_root/
├── factuur/
│   ├── config/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
└── venv/
```

Create a virtual environment
```
python -m venv venv
```


Activate the virtual environment

```
Windows:
    .\venv\Scripts\activate
Unix or Linux:
    source venv/bin/activate
```
Install the dependencies

```sh
pip install -r requirements.txt
```

Configure migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

Start server
```
python manage.py runserver
```

## Project Structure
If you have successfully launched a project, you will start developing it. 
Project files are located in project folders.

- The settings.py file contains project settings, such as the database, paths to static files, project language, etc.
- The urls.py file contains the addresses of the project pages.
- The views.py file contains the project logic.
- The models.py file contains the database models.
- The admin.py allows you to register models that will be available in the admin interface. 
- The serializers.py contains code for serializing and deserializing complex data types, such as models.
- The permissions.py file contains the permissions classes for the Django REST framework.
- The templates folder contains HTML page templates.
- The static folder contains static files such as CSS styles, JavaScript scripts, etc.
- The migrations folder contains database migrations.



