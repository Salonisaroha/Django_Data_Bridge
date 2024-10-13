
# Django REST API with Viewsets and Serializers

This repository contains a Django project that demonstrates the use of REST APIs with Django, utilizing Django REST Framework's powerful features like serializers and viewsets to handle data representation and rendering. 


## Features

**RESTful API**: The project uses Django REST Framework to create a fully functional REST API.
- **Serializers**: Converts complex data types like Django QuerySets and model instances into JSON, making it easy to render data in API responses.
- **Viewsets**: Simplifies the logic for handling CRUD operations (Create, Read, Update, Delete) by grouping related views into a single class.
- **Model-based Design**: Uses Django's ORM for easy data manipulation and retrieval.
- **Permission Handling**: Supports customizable permission classes for managing access to different API endpoints.
- **Browsable API**: Includes a browsable web-based API interface that makes it easy to test and interact with the API.


## Tech Stack

**Django**: High-level Python web framework used to build the project.
- **Django REST Framework**: Toolkit for building Web APIs in Django.
- **Python**: Programming language used for development.
- **Sqlite3**: Database for storing and managing data (you can specify your choice).


## Project Structure

- `models.py`: Defines the data models for the application.
- `views.py`: Contains viewsets that handle the API logic.
- `serializers.py`: Defines serializers to convert Django model instances to JSON and vice versa.
- `urls.py`: Maps URL endpoints to the appropriate viewsets for handling requests.

