Chatbot Moderator
=================

**Chatbot Moderator** provides ....


Please refer to the following documents for details:

* [Solution Requirements](doc/requirements/requirements-overview.md)
* [Project Use Cases](doc/requirements/usecases.md)
* [Project Architecture Document](doc/architecture/architectural-overview.md)
* [Project Data Model](doc/architecture/architectural-data-view.md)
* [Server README](server/README.md)

# Developing

Please refer to the server's [README](server/README.md) for details about developing the server web-app.

# Deploying

Docker Compose can be used to build and deploy the solution.

`./run-docker.sh`

* `run-docker.sh` echos instructions for creating self-signed certificates to STDOUT.

If the build fails due to a DNS error while installing dependencies with Pipenv you should ensure that additional DNS settings have been configured for Docker.

```$ cat /etc/docker/daemon.json
{
    "dns": ["8.8.8.8", "152.3.72.100", "152.3.70.100"]
}
$ sudo service docker restart
```

----

 Copyright 2020, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.
