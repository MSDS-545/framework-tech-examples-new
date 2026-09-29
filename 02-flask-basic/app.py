"""
Simple Flask Web Application + API Example

This example demonstrates:
1. Creating a Flask application
2. Creating a normal webpage route
3. Creating a GET API endpoint
4. Creating a POST API endpoint
5. Returning JSON from an API
6. Receiving JSON from a client
"""

# Flask creates the web application.
# jsonify() converts Python data into a JSON HTTP response.
# request gives us access to information sent by the client.
# render_template() loads an HTML template.
from flask import Flask, jsonify, request, render_template


# Create the Flask application.
#
# __name__ tells Flask where this application
# is located so it can find resources such as templates.
app = Flask(__name__)


# ---------------------------------------------------------
# WEBPAGE ROUTE
# ---------------------------------------------------------

@app.route("/")
def home():
    """
    Display the application's home page.

    When the browser requests:
        http://127.0.0.1:5000/

    Flask calls this function.
    """

    # Flask searches the templates/ directory
    # for index.html.
    return render_template("index.html")


# ---------------------------------------------------------
# GET API ENDPOINT
# ---------------------------------------------------------

@app.route("/api/course", methods=["GET"])
def get_course():
    """
    Return course information as JSON.

    A GET request is normally used to retrieve data.
    """

    # Regular Python dictionary.
    course = {
        "course": "Web Framework Example",
        "framework": "Flask",
        "language": "Python"
    }

    # Convert the dictionary into a JSON response.
    return jsonify(course)


# ---------------------------------------------------------
# POST API ENDPOINT
# ---------------------------------------------------------

@app.route("/api/message", methods=["POST"])
def create_message():
    """
    Receive JSON from the client and return a response.

    A POST request is commonly used when the client
    sends new information to the server.
    """

    # Read JSON from the HTTP request body.
    data = request.get_json()

    # Retrieve the "name" field.
    #
    # If the client does not provide a name,
    # use "Student" as the default value.
    name = data.get("name", "Student")

    # Create the response.
    response = {
        "message": f"Hello, {name}!",
        "framework": "Flask"
    }

    # Return JSON and HTTP status code 201.
    #
    # 201 means that a resource/request was
    # successfully created.
    return jsonify(response), 201


# ---------------------------------------------------------
# START APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    # Start Flask's development server.
    #
    # debug=True automatically reloads the application
    # when source code changes and provides debugging
    # information during development.
    app.run(debug=True)