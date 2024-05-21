# Lab Work No. 1

## Task

Write two Dockerfiles – a bad one and a good one...

## Main Part

Let's consider working with containers using the example of a Go program that prints the line "Hello, world!".

```go
package hello

import "fmt"

func main() {
	fmt.Println("Hello, world!")
}
```

### Creating a Bad Dockerfile

The contents of the bad Dockerfile are presented below:

```dockerfile
FROM ubuntu:latest

# creating a new directory
WORKDIR /app

# installing golang
RUN apt-get update
RUN apt-get -y install golang

# copying all files from the project directory
COPY . .

# building the package
RUN go build -o main

CMD ["./main"]
```

### Bad Practice 1

Using a suboptimal base image:

```dockerfile
FROM ubuntu:latest
```

An image based on the Ubuntu distribution contains additional software that will not be used when running the considered container. In this case, it is better to use a more specific golang image, which supports all the necessary functionality but is significantly lighter.

It is also not recommended to use the latest tag, as the appearance of a new version of the base image during the build can lead to errors. It is always worth specifying a specific version of the image.

### Bad Practice 2

As a result of using an image based on ubuntu, there is a need to install Go to perform the project build.

```dockerfile
RUN apt-get update 
RUN apt-get -y install golang
```

Each RUN instruction is executed on a new layer, which increases overhead. Also, the result of the `apt-get update` command will be cached, and when executing the `apt-get -y install golang` command, an outdated version of the package may be installed.

In addition, it is better to clear the apt cache in the /var/lib/apt/lists directory to reduce the image size.

Thus, in this case, it is better to write:

```dockerfile
RUN apt-get update && apt-get install -y golang \
  && rm -rf /var/lib/apt/lists/*
```

### Bad Practice 3

In the bad Dockerfile, all files from the project directory are copied into the container, although only the executable file is needed to run the container.

```dockerfile
COPY . .
```

Unnecessary files increase the amount of memory occupied by the container. It is better to use a multi-stage build to reduce the size of the final image.

### Bad Practices in Container Usage

1. You cannot store data inside containers, as they can be stopped or destroyed at any moment. If you need to save data, you should use volumes. Moreover, volumes are often a better choice than saving data in the container's writable layer, as a volume does not increase the size of the containers using it, and the contents of the volume exist outside the lifecycle of the given container.
2. You cannot specify account data inside the Dockerfile, as this data can be disclosed when adding the Dockerfile to a GitHub repository or when uploading the image to Docker Hub. For this purpose, you should use environment variables, which can be set when starting the container using the -e flag.
