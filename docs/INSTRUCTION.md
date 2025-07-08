# INSTRUCTIONS.md

This guide will help you **run**, **test**, and **deploy** this project after cloning the repository.

---

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.10 or higher**
- **Docker (with docker-compose)**
- **AWS credentials**

---

## Getting Started

### 1. Clone the Repository

```bash
git https://github.com/ofek55676/secure-transfer-poc.git
cd devops-challenge
```

### 2. Create a .env File
In the root of the project, create a file named .env and add your AWS credentials:
```
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region
DYNAMODB_TABLE_NAME: your-dynamodb-table
CODE_NAME: your-code-name
DOCKERHUB_URL: your-dockerhub-url
GITHUB_URL: your-github-url
```
⚠️ Make sure this file is not committed to version control.

### 3. Run the Application with Docker (Locally)
Build and start the application using Docker Compose:
```
docker-compose up --build -d
```

### 4. Run Unit Tests Locally
Step 1: Install Python dependencies
```
pip install -r requirements.txt
```
Step 2: Run the tests
```
pytest 
```

### Continuous Integration (Travis CI)
When you push to the master branch Travis installs dependencies, runs all tests, builds and pushes the Docker image to Docker hub.

These must be set in your Travis CI project Environment Variables (Docker Personal Access Token):

```
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-password
```

### FastAPI Server
Once your docker running, you can access:

```
http://127.0.0.1:5000/health → API status and metadata
http://127.0.0.1:5000/secret → Fetches a secret value from DynamoDB
```
