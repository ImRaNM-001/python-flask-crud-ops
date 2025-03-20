# Python Flask CRUD API Project

## Overview
A lightweight, containerized REST API application built with Flask demonstrating best practices for creating, reading, updating, and deleting resources. This project showcases efficient data handling, authentication systems, and responsive user interfaces.

## Technologies Used
- **Flask**: Lightweight WSGI web application framework
- **Python**: Core programming language
- **Werkzeug**: WSGI utility library used by Flask
- **Jinja2**: Template engine for dynamic HTML generation
- **Flask-RESTful**: Extension for building REST APIs
- **Flask-JWT-Extended**: Authentication and authorization
- **Pytest**: Testing framework for unit and integration tests
- **Docker**: Containerization for consistent deployment
- **GitHub Actions**: CI/CD pipeline for automated testing and container publishing
- **Requests**: HTTP client library for API operations and testing
- **Git**: Version control

## Features
- RESTful API endpoints
- User authentication and authorization
- Complete CRUD operations (Create, Read, Update, Delete)
- JSON request/response handling
- Error handling with appropriate HTTP status codes
- Blueprint-based route organization
- Template rendering with Jinja2
- Form handling
- Containerized application with Docker
- Comprehensive test coverage

## Setup Instructions
1. Clone the repository

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python3 flask_crud_ops.py
   ```

## Running with Docker
```
docker build -t python-flask-crud-ops:v1 .
docker run -p 3100:3100 python-flask-crud-ops:v1
```
or,

```
docker build -t python-flask-crud-ops:v1 .
docker images                       # and grab the image id
docker run -p 3100:3100 <image-id>
```

## Push a new image manually to **GitHub Container Registry**
Step 1. Login to GitHub Container Registry:
   ```bash
   # Set your PAT as an environment variable first
   export GITHUB_PAT=your_personal_access_token
   ```

   ```bash
   # Then login using the environment variable (no token exposed in command history)
   docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin < <(printf "%s" "$GITHUB_PAT")

   # Example:
   docker login ghcr.io -u JohnDoe-007 --password-stdin < <(printf "%s" "$GITHUB_PAT")
   ```

Step 2. Build the Docker Image and tag it with a version:
   ```
   docker build -t ghcr.io/johndoe-001/python-flask-crud-ops:v2 .
   ```
Step 3. Push the build image to GHCR.io registry:
   ```
   docker push ghcr.io/johndoe-001/python-flask-crud-ops:v2
   ```

Step 4. Remove the environment variable once done and clear the shell history:
   ```
   unset GITHUB_PAT
   
   history -c                 #Clear current session history (Bash)
   ```

## API Endpoints
- **GET /items**: Retrieve all items
- **GET /items/{id}**: Retrieve a specific item
- **POST /items**: Create a new item
- **PUT /items/{id}**: Update an existing item
- **DELETE /items/{id}**: Delete an item

## Testing
Run the test suite:
```
python -m pytest -vs tests/test_flask_crud_ops.py
```

## Project Structure
- `flask_crud_ops.py`: Main CRUD API implementation
- `app.py`: Basic Flask application with blueprints
- `main.py`: Alternative Flask app with different routing
- `form_post.py`: Flask app demonstrating form handling
- `jinja_2_*.py`: Template rendering with Jinja2
- `api_operations.py`: External API consumption with requests
- `tests/`: Test files for the application
- `templates/`: HTML templates for rendering

## CI/CD
The project uses GitHub Actions for continuous integration and deployment:
- Automated testing with pytest
- Docker image building and publishing to GitHub Container Registry



## For Production environments, use a WSGI Server (Web Server Gateway Interface) like **"Gunicorn"**

### What is WSGI?

WSGI (Web Server Gateway Interface) is a specification that describes how a web server communicates with a web application in Python. It's essentially a standard interface between web servers and Python web applications or frameworks.

### What is Gunicorn?

Gunicorn (Green Unicorn) is a production-ready WSGI HTTP server for Python web applications. It:

- Is designed to serve Python WSGI applications like Flask
- Manages multiple worker processes to handle concurrent requests
- Offers better performance, stability, and resource management compared to Flask's development server
- Is production-ready and battle-tested

### Why use Gunicorn instead of Flask's development server?

1. **Performance**: Gunicorn can handle multiple requests concurrently using worker processes
2. **Stability**: Designed to recover from errors and continue serving
3. **Security**: Flask's development server has security vulnerabilities not suitable for production
4. **Resource management**: Better handles memory and CPU resources


### How to use Gunicorn with your Flask app:

1. Install Gunicorn:
   ```bash
   pip3 install gunicorn
   ```

2. Run your Flask app with Gunicorn:
   ```bash
   gunicorn --bind 0.0.0.0:3100 --timeout 120 flask_crud_ops:app
   ```

3. For Docker, update the Dockerfile to use Gunicorn:
   ```dockerfile
   # Command to run when container starts

   CMD ["gunicorn", "--bind", "0.0.0.0:3100", "--timeout", "120", "flask_crud_ops:app"]
   ```

## API Documentation
API documentation is available at [/api/docs](https://flask.palletsprojects.com/en/stable/api/).

## License
MIT