# Lab Work No. 2

## Task

Create a `docker-compose.yml` file with a minimum of three services.

## Solution Description

This lab work involved creating a `docker-compose.yml` file based on the `dockerspawner` repo from JupyterJub. The compose file orchestrates three services: an initialization service (`init-hub`), an Jupyter Hub (`hub`), and a database (`postgres`).

![Compose Up](/images/ComposeUp.png)
![Hub](/images/Hub.png)

## Questions and Answers

- **Can you limit resources (such as memory or CPU) for services in docker-compose.yml? If not, why? If so, how?**

  Yes, you can limit resources for services in `docker-compose.yml`. This can be done using the `deploy` key under each service, which allows you to specify resource constraints like memory and CPU limits. However, these settings are only effective when deploying to a swarm with `docker stack deploy` and are ignored by `docker-compose up` and `docker-compose run`. To apply these limits during development with `docker-compose`, you can use the `--compatibility` flag⁵.

  Example:
  ```yaml
  services:
    my-service:
      image: my-image
      deploy:
        resources:
          limits:
            cpus: '0.50'
            memory: 50M
  ```

- **How can you start only a specific service from docker-compose.yml without starting the others?**

  You can start a specific service by using the `docker-compose up` command followed by the service name. This will start the specified service and any other services it depends on. If you want to start a service without starting its dependencies, you can use the `--no-deps` flag¹.

  Example:
  ```bash
  docker-compose up --no-deps my-service
  ```

## Dependencies

- Docker
- Docker Compose
