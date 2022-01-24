# SUchedule Service
This code repository allows you to pull information about Sabancı University lessons information.

## Installation

**Be sure to use the same version of the code as the version of the docs you're reading.**
You probably want the latest tagged version, but the default Git version is the master branch.

```shell
# clone the repository
$ git clone https://github.com/furkankyildirim/SUchedule_Service
$ cd SUchedule_Service
# checkout the correct version
$ git tag
```

Create a virtualenv and activate it:
```shell
$ python3 -m venv venv --without-pip
$ source venv/bin/activate
```

Install pip3 requirements
```shell
$ pip3 install -r requirements.txt
```

## Run

### Run Service on Flask
```shell
$ export FLASK_APP=Service 
# to run in developer mode
$ export FLASK_ENV=development
$ flask run
```
Or on Windows cmd:
```shell
$ set FLASK_APP=Service
# to run in developer mode
$ set FLASK_ENV=development
$ flask run
```
Open http://127.0.0.1:5000 in a browser.
### Run Service on Gunicorn 

```shell
# if your service does not have Gunicorn server
$ pip3 install gunicorn
$ ./runner.sh
# to the service to run in the background
$ ./runner.sh &
```

## Edit Config File
Edit the [config.ini](https://github.com/furkankyildirim/SUchedule_Service/tree/master/config.ini) file so that the program can run on your own computer.
```text
[Service]
host = Your_hostname
port = Your_portname
```
Edit the [runner.sh](https://github.com/furkankyildirim/SUchedule_Service/tree/master/runner.sh) file so that the program can run on your gunicorn service
```text
NUM_WORKERS=3
TIMEOUT=600

exec gunicorn Service:app \
--workers $NUM_WORKERS \
--timeout $TIMEOUT \
--log-level=debug \
--bind=127.0.0.1:5000 \
```

## Common Issues
If you cannot to connect to your server:
```shell
$ kill $(lsof -t -i:your_portname)
```
If you get the error (Permission denied) when try to run runner.sh
```shell
$ chmod +x runner.sh
```
