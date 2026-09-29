"""
Basic FastAPI Example

This example demonstrates:
1. Creating a FastAPI application
2. Creating a GET endpoint
3. Using a path parameter
4. Creating a POST endpoint
5. Using Pydantic for request validation
6. Testing the API through Swagger UI
"""

# FastAPI is the web framework used to create the API.
from fastapi import FastAPI

# BaseModel is used to define and validate
# the structure of incoming JSON data.
from pydantic import BaseModel


# ---------------------------------------------------------
# CREATE THE FASTAPI APPLICATION
# ---------------------------------------------------------

# Create the main FastAPI application object.
#
# The title appears in the automatically generated
# Swagger API documentation.
app = FastAPI(
    title="FastAPI Classroom Example"
)


# ---------------------------------------------------------
# REQUEST DATA MODEL
# ---------------------------------------------------------

class MessageRequest(BaseModel):
    """
    Define the JSON structure expected by the
    POST /message endpoint.

    FastAPI automatically validates incoming JSON
    against this model.
    """

    name: str


# ---------------------------------------------------------
# ROOT ENDPOINT
# ---------------------------------------------------------

@app.get("/")
def home():
    """
    Simple GET endpoint.

    Visiting:
        http://127.0.0.1:8000/

    causes FastAPI to execute this function.
    """

    # Returning a Python dictionary automatically
    # produces a JSON HTTP response.
    return {
        "message": "Hello from FastAPI!"
    }


# ---------------------------------------------------------
# COURSE ENDPOINT
# ---------------------------------------------------------

@app.get("/course")
def get_course():
    """
    Return information about the example application.
    """

    return {
        "course": "Web Framework Example",
        "framework": "FastAPI",
        "language": "Python"
    }


# ---------------------------------------------------------
# PATH PARAMETER EXAMPLE
# ---------------------------------------------------------

@app.get("/hello/{name}")
def say_hello(name: str):
    """
    Demonstrate a FastAPI path parameter.

    Example:
        /hello/Alex

    FastAPI extracts "Alex" from the URL
    and passes it to the name parameter.
    """

    return {
        "message": f"Hello, {name}!"
    }


# ---------------------------------------------------------
# POST ENDPOINT
# ---------------------------------------------------------

@app.post("/message")
def create_message(data: MessageRequest):
    """
    Receive JSON from the client.

    Expected JSON:

        {
            "name": "Alex"
        }

    FastAPI validates the request using
    MessageRequest before this function runs.
    """

    return {
        "message": f"Hello, {data.name}!",
        "framework": "FastAPI"
    }