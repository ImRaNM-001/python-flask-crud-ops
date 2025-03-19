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
docker build -t flask-crud-api . docker run -p 3100:3100 flask-crud-api
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

## API Documentation
API documentation is available at [/api/docs](https://flask.palletsprojects.com/en/stable/api/).

## License
MIT