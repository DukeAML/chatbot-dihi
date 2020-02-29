Chatbot Moderator
=================

The **Chatbot Moderator Server** is a Flask web-app which provides a RESTful interface and web application. Details about these interfaces can be found in the project's architecture's [data](../doc/architecture/architectural-data-view.md) and [implementation](../doc/architecture/architectural-implementation-view.md) views.

# Getting Started

## Installation

The server depends upon [pipenv](https://github.com/pypa/pipenv) for its Python environment.

1. Make sure you have `pipenv` installed
2. Install requirements with `pipenv install`
3. Create self-signed certificates with `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

## Deployment

The server source code includes two scripts for starting the server:

* `dev.sh` starts the development server using Flask. This is not suitable for the production environment.
* `pipenv boot` starts the server using Gunicorn. Gunicorn should be fronted by a reverse proxy. A sample Nginx configuration for establishing a reverse proxy can be found in the project's `client/nginx/project.conf`.
* `pipenv bootssl` starts the server using Gunicorn with HTTPS. Gunicorn should be fronted by a reverse proxy. A sample Nginx configuration for establishing a reverse proxy can be found in the project's `client/nginx/project-ssl.conf`.

## Testing the app

* Run `sslyze 127.0.0.1:9999 --regular` to check the HTTPS configuration of Gunicorn.

* Run `pipenv run pytest` to execute the unit tests.

## Developing

1. Make sure you have `pipenv` installed
2. Install requirements with `pipenv install --dev`

**Strings**

The server returns string content to the client. All string content returned for display to the client can be found in `locales/en/LC_MESSAGES/base.po`. After editing this file `pipenv strings` **MUST** be executed to generate the binary `.mo` files.

