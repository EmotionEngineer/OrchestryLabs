# Lab Work No. 3 - Nextcloud & PostgreSQL

## Description

This project involves deploying the Nextcloud cloud storage service using a PostgreSQL database

## Project Deploy

To deploy the project, execute the following commands:

```bash
kubectl create -f pg_configmap.yml
kubectl create -f pg_secret.yml
kubectl create -f pg_service.yml
kubectl create -f pg_deployment.yml
kubectl create -f nextcloud.yml
```

## Workflow

The following steps were taken during the workflow:

1. Starting Minikube to create a local Kubernetes cluster.
2. Using kubectl to manage Kubernetes resources.
3. Checking the status of the pods and their proper functioning.

## Visualization of Work

- Minikube start:
![Minikube Start](Screen/Minikube.png)

- Kubectl deploy:
![Kubectl Commands](Screen/Kubectl.png)

- Pods status:
![Pods Status](Screen/Pods.png)

## Questions and Answers

1. **Is the order of manifest execution important?**

   Yes, the order is important. Configurations and secrets should be created first to avoid errors when deploying the deployment due to their absence.

2. **What will happen if you scale the replicas of postgres-deployment to 0 and then back to 1?**

   Setting the number of replicas to 0 will delete the pod, and Nextcloud will not be able to connect to the database, leading to errors. Restoring the replicas to 1 will allow Nextcloud to re-establish the connection and continue to operate normally.
