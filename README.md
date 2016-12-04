# Polls django App

Python web project developed using Django framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python 3.*
django 1.10.*
mysql 5.*

### Installing - Using Pip

python3 -m pip install mysqlclient
python3 -m pip install setuptools
python3 -m pip install django

### Setup mysql

CREATE USER 'root'@'localhost' IDENTIFIED BY '';
create database djangodb;

## Running the migrations

python manage.py migrate

### Up and Running

```
python manage.py runserver
```

## Accessing admin page

access http://127.0.0.1:8000/admin/ create some questions and choices

### Accessing the web app page

access http://127.0.0.1:8000/polls/ to see the dashboard results

## Running unit test

```
python manage.py test polls
```

## Authors

* **Elton Jhony** - *Initial work* - [PurpleBooth](https://github.com/EltonOl)
