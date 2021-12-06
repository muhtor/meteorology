# Meteorology

Django server.

### How to clone project

```
git clone https://github.com/muhtor/meteorology.git
```
## Guide for developers

Run django on development:
```
python manage.py runserver --settings=meteorology.settings.production
python manage.py makemigrations --settings=meteorology.settings.production
python manage.py migrate --settings=meteorology.settings.production
```


# DOCKER

### Django commands

Running migrations with docker-compose (if `run` is used instead of `exec`, then new container is created instead of using the existing one - hence it's better to use `exec`)
```
docker-compose exec meteweb python manage.py makemigrations
docker-compose exec meteweb python manage.py migrate
docker-compose exec meteweb python manage.py createsuperuser
```

### Create new JOB

http://127.0.0.1:2020/admin/queues/job/


### Other commands

Deleting all images and containers (dangerous please use it with caution)
```
docker system prune -a --volumes
```

```
docker images
docker container ls
```