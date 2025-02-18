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
