# Secure Transfer Project
A lightweight API server that retrieves a secret code from DynamoDB.

## API Server
This project implements a simple web service that returns a secret code and provides a health check endpoint.

The application is built using **Python** and the **FastAPI** framework.

#### Why FastAPI?
1. **High Performance**: One of the fastest Python web frameworks.
2. **Powerful Dependency Injection** – Clean and intuitive for managing configuration and services.
3. **Type Hints Support** – Full integration with Pydantic for robust data validation.
4. **Developer Friendly** – Minimal learning curve with excellent documentation and tooling.

## Architecture
The project follows a simplified **Three-Tier Architecture**:

1. **Application Layer** – Exposes HTTP endpoints using FastAPI.
2. **Business Logic Layer** – Handles core logic and interacts with the data layer.
3. **Data Access Layer** – Performs CRUD operations on DynamoDB.

> ⚠️ Note: In this project, the **data access** and **business logic** layers are merged due to the small scope. 

### Tests
This project uses **Pytest** for writing and running tests.

I use fixture to configure a reusable FastAPI test client, which allows me to simulate requests to the API without starting the server.

Since the `/secret` endpoint connects to DynamoDB, I use pytest and patch to mock the database interaction.

### Docker
Using `python:3.13-alpine` as a lightweight base image to reduce the attack surface.

Infrequent instructions (like installing packages) are placed before frequently changing ones (like `COPY`) to improve Docker layer caching and reduce rebuild time.

### Trvis CI
This project uses **Travis CI** to automate testing, building, and deploying a Dockerized FastAPI application.

### CloudFormation
This project uses **CloudFormation** to deploy the service on ECS. ECS is a best practice for running long-lived containers without the overhead of managing the underlying infrastructure, although it is slightly less flexible.

Security Recommendations:

1. Remove the access key from the container and use an IAM Role attached to the ECS Task instead.

2. Do not deploy this service in a public subnet — the secret code could be exposed to the internet.

3. Add authentication to the FastAPI application to restrict access.

4. Ensure the Application Load Balancer (ALB) is exposed only over HTTPS.

5. Forward logs to a centralized logging system to audit access to the secret.