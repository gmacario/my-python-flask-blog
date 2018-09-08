# my-python-flask-blog

Based on the blog post "[Scriviamo un blog in Python e Flask](https://ludusrusso.cc/2016/12/27/tutorial-flask/)" by [Ludus Russo](https://ludusrusso.cc/) who in turn took ispiration from [Miguel Grindberg](https://blog.miguelgrinberg.com/).

### Usage Examples

#### Build Docker image

```shell
docker build -t my-python-flask-blog .
```

#### Print command line help

```shell
docker run --rm my-python-flask-blog python3 manage.py -?
```

#### Launch a Python shell inside the Flask application

```shell
docker run -ti --rm my-python-flask-blog python3 manage.py shell
```

#### Run a development webserver

```shell
docker run -d --rm -p 5000:5000 my-python-flask-blog
```

You may access the server locally at <http://localhost:5000>

To inspect the running container type the following command:

```shell
docker exec -ti $CONTAINER_ID /bin/bash
```

#### Run a production webserver

TODO

### License and Copyright

my-python-flask-blog is licensed under the MIT License - for details please see the [LICENSE](LICENSE) file.

Copyright (C) 2018, [Gianpaolo Macario](https://gmacario.github.io/)

<!-- EOF -->
