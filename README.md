# News Notifications Publisher-Subscriber Distributed System

The purpose of this project is to use the publisher subscriber model to provide all subscribers news highlights notifications. Users will be able to subscribe to a certain type of news or a specific topic of news. The publisher will retrieve the latest news data from the internet. On a regular basis, the publisher will provide a list of the latest news.

'Pub/sub' systems use an intermediary to distribute events to numerous receivers (called subscribers).  We'll use Docker containers to simulate a pub/sub system in this project.

Technologies used:
Python 
Node.js
Docker
To install follow the steps given here https://docs.docker.com/get-docker/

```
$ docker --version   #checking if docker is installed perfectly
```

## Frontend

First go the `newsnotifications` directory. Then run the below commands:

```
docker build -t newsnotification-image:v1 #create new image for newsnotification application
docker run -d -p 80:80 --name newsnotification_central newsnotification-image:v1
```

The application should be running on `https:\\localhost:80 `

## Backend 

Go the `newsnotifications` directory. Then run the below commands:

```
docker-compose up
```


## Additional Documentation

.. image:: https://img.shields.io/pypi/v/newsnotifications.svg
        :target: https://pypi.python.org/pypi/newsnotifications

.. image:: https://img.shields.io/travis/yash26195/newsnotifications.svg
        :target: https://travis-ci.com/yash26195/newsnotifications

.. image:: https://readthedocs.org/projects/newsnotifications/badge/?version=latest
        :target: https://newsnotifications.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
