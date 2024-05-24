# Real Time Analysis Assignment - Warsaw School of Economics

This project is a Real Time Analysis class assignment at the Warsaw School of Economics. It demonstrates the use of Flask, Docker, and a simple Perceptron model to provide predictions via a REST API.

## Features

-   Flask-based web application
-   Simple Perceptron model for predictions
-   Dockerized for easy deployment

## Requirements

-   **Docker**
-   **Python 3.7 or higher**

## Setup Instructions

### Running as a Docker Container

1.  **Clone the repository:**

    ``` bash
    git clone https://github.com/MichalPoleszczuk/FlaskPerceptron-DockerApp.git
    cd FlaskPerceptron-DockerApp/docker
    ```

2.  **Build the Docker image:**

    ``` bash
    docker build -t perceptron-flask-app .
    ```

3.  **Run the Docker container:**

    ``` bash
    docker run -p 5000:5000 perceptron-flask-app
    ```

4.  **Test the API:**

    You can test the API using `curl`:

    ``` bash
    curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input": [1, 2]}'
    ```

## File Descriptions

-   **app.py:** This is the main Flask application that defines two routes:

    -   `/`: A simple route that returns "Hello, World!".
    -   `/predict`: A POST route that accepts a JSON payload with an input array and returns a prediction from a simple Perceptron model.

-   **Dockerfile:** This file contains the instructions to build a Docker image for the Flask application. It sets up the Python environment, installs dependencies, and runs the Flask app.

-   **requirements.txt:** This file lists the Python dependencies required for the Flask application, including Flask and NumPy.
