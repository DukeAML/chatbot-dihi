# Copyright 2020, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

from python:3.7

# create a non-root user
RUN addgroup app
RUN adduser --ingroup app app

# create and populate the project directory
RUN mkdir -p /home/project/chatbot
RUN chown -R app:app /home/project/chatbot
COPY --chown=app:app . /home/project/chatbot

# change to the non-root user
USER app:app

# include pip installed things into the user's path
ENV PATH="/home/app/.local/bin:${PATH}"

# install project dependencies
WORKDIR /home/project/chatbot
RUN pip install pipenv --user
RUN pipenv install --dev

# copy certificates & keys
COPY ./key.pem /etc/ssl/key.pem
COPY ./cert.pem /etc/ssl/certificate.pem

# define a health check for the container
HEALTHCHECK --timeout=5s CMD curl -k --fail https://localhost:9999/status || exit 1
