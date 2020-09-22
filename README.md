1- Make sure that docker group exists with sudo 
        link : https://docs.docker.com/engine/install/linux-postinstall/

2- Make sure that redis server is running port 6379


3- run celery worker localy-to view celery-:
        $ celery -A task  worker -l info
