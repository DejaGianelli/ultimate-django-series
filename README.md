# STOREFRONT

## Setting up Development Environment 

### Python Env

Create a new virtual environment

```shell
$ pipenv install
```

Activate the virtual environment

```shell
$ pipenv shell
```

### Get database up and running

Mysql database and Adminer (GUI) for development is available using docker by running:

```shell
$ docker compose up
```

### Running Migrations

```shell
$ python manage.py migrate
```

### Running the Application Server

```shell
$ python manage.py runserver
```


