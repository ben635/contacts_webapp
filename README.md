# Contacts Webapp

This README provides instructions for running the webapp using Docker and an alternative method using pipenv and Python.

## Running with Docker

1. **Download and Install Docker**
    - Visit [Docker's official website](https://www.docker.com/get-started) and follow the installation instructions for your operating system.

2. **Build the Docker Image**
    - Open a terminal in the top level directory of the repo.
    - Run the following command to build the Docker image:
      ```
      docker build -t contacts_webapp .
      ```

3. **Run the Docker Container**
    - Start the container using the command:
      ```
      docker run -p 8000:8000 contacts_webapp
      ```
    - Access the webapp at: [http://localhost:8000/front/contacts](http://localhost:8000/front/contacts)

## Running with pipenv and Python

1. **Install Python**
    - Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Set Up pipenv**
    - Install pipenv if you haven't already:
      ```
      pip install pipenv
      ```

3. **Install Dependencies**
    - In the root directory of the project, run:
      ```
      pipenv install --deploy --ignore-pipfile
      ```

4. **Run the Webapp**
    - Activate the virtual environment:
      ```
      pipenv shell
      ```
    - Run the Django development server:
      ```
      python manage.py runserver 0.0.0.0:8000
      ```
    - Access the webapp at: [http://localhost:8000/front/contacts](http://localhost:8000/front/contacts)

    ## CI/CD and Cloud Deployments

    This section outlines how to integrate CI/CD workflows for deploying the webapp on cloud platforms using container services.

    ### AWS

    - Integrate with AWS CodePipeline or GitHub Actions.
    - Build your Docker image and push it to Amazon ECR.
    - Deploy using services like AWS Fargate or Amazon ECS/EKS.
    - Example GitHub Actions snippet:
        ```
        name: Build and Deploy to AWS

        on:
            push:
                branches: [ main ]

        jobs:
            build:
                runs-on: ubuntu-latest
                steps:
                    - uses: actions/checkout@v2
                    - name: Build Docker image
                        run: docker build -t contacts_webapp .
                    - name: Login to AWS ECR
                        run: |
                            aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
                    - name: Tag and Push to ECR
                        run: |
                            docker tag contacts_webapp:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/contacts_webapp:latest
                            docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/contacts_webapp:latest
        ```

    ### GCP

    - Use Cloud Build or GitHub Actions for your CI/CD pipeline.
    - Build the Docker image and push it to Google Container Registry (GCR).
    - Deploy to Cloud Run or Google Kubernetes Engine (GKE).
    - Example step using Cloud Build:
        ```
        steps:
            - name: 'gcr.io/cloud-builders/docker'
                args: ['build', '-t', 'gcr.io/$PROJECT_ID/contacts_webapp', '.']
            - name: 'gcr.io/cloud-builders/docker'
                args: ['push', 'gcr.io/$PROJECT_ID/contacts_webapp']
        ```

    ### Azure

    - Leverage Azure Pipelines or GitHub Actions for automated deployments.
    - Build the Docker image and push it to the Azure Container Registry (ACR).
    - Deploy using Azure Container Instances (ACI) or Azure Kubernetes Service (AKS).
    - Example Azure Pipelines snippet:
        ```
        trigger:
            branches:
                include:
                    - main

        pool:
            vmImage: 'ubuntu-latest'

        steps:
        - task: Docker@2
            displayName: Build and push image to ACR
            inputs:
                command: buildAndPush
                repository: contacts_webapp
                dockerfile: '**/Dockerfile'
                containerRegistry: '<Azure_Container_Registry_Service_Connection>'
                tags: |
                    $(Build.BuildId)
        ```