=================
NewsNotifications
=================


.. image:: https://img.shields.io/pypi/v/newsnotifications.svg
        :target: https://pypi.python.org/pypi/newsnotifications

.. image:: https://img.shields.io/travis/yash26195/newsnotifications.svg
        :target: https://travis-ci.com/yash26195/newsnotifications

.. image:: https://readthedocs.org/projects/newsnotifications/badge/?version=latest
        :target: https://newsnotifications.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Implementing various algorithms learnt as a part of distributed systems to create a pub-sub news notification service


* Free software: MIT license
* Documentation: https://newsnotifications.readthedocs.io.


Features
--------

# Pub-Sub-Distributed-System-Using-Docker

Publish/Subscribe (or pub/sub for short) is a popular **indirect** communication system. `Pub/sub` systems disseminates events to multiple recipients (called subscribers) through an intermediary. Examples of successful pub/sub include `Twitter` and `Bloomberg terminal`-like financial systems. In this project, we will emulate a pub/sub system using `Docker` which is a computer program that performs operating-system-level virtualization, also known as "containerization".

# How to start with docker

You will need to install **docker** if you do not have it already.

```
$ sudo snap install docker
$ docker --version   #checking if docker is installed perfectly

```

`(Distributed Publisher/Subscriber System with a Decentralized Server)`

Frontend
First go the `newsnotifications` directory. Then run the below commands:

```
docker build -t pubsub-image:v1 #create new image for pubsub application
docker run -d -p 80:80 --name pubsub_central pubsub-image:v1
```
Now go to url `localhost:80` to see the output of the app from docker.

Backend 
`(Distributed Publisher/Subscriber System with distributed servers)`

First go the `newsnotifications` directory. Then run the below commands:

```
docker-compose up

```

If you want to stop the servers, then press `Ctrl+C`

---
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**


* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
