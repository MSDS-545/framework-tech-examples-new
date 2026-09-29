# 03 --- FastAPI Basic Example

This example demonstrates a basic **FastAPI REST API**.

It introduces:

-   typed API endpoints;
-   path parameters;
-   Pydantic validation;
-   JSON responses;
-   automatic OpenAPI documentation;
-   interactive Swagger UI documentation.

The example is intentionally small so students can focus on how a
request moves from a client to a FastAPI route and back as a JSON
response.

------------------------------------------------------------------------

## 1. Basic Architecture

The request flow is:

``` text
Browser / API Client
        |
        | HTTP Request
        v
     FastAPI
        |
        v
  Path Operation
   Function
        |
        v
 Python / Pydantic
      Logic
        |
        v
 JSON Response
        |
        v
Browser / API Client
```

FastAPI automatically converts compatible Python return values into JSON
responses.

------------------------------------------------------------------------

## 2. Project Structure

A simplified project structure is:

``` text
03-fastapi-basic/
├── main.py
├── requirements.txt
└── README.md
```

The FastAPI application is defined in:

``` text
main.py
```

A typical application begins with:

``` python
from fastapi import FastAPI

app = FastAPI()
```

The variable:

``` text
app
```

is the FastAPI application object used by Uvicorn.

------------------------------------------------------------------------

## 3. Create a Virtual Environment

From inside the `03-fastapi-basic` directory:

``` bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

``` bash
source .venv/bin/activate
```

On Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

Verify the active Python:

``` bash
python --version
```

On macOS/Linux:

``` bash
which python
```

The path should point inside `.venv`.

------------------------------------------------------------------------

## 4. Install the Dependencies

Upgrade pip:

``` bash
python -m pip install --upgrade pip
```

Install the project requirements:

``` bash
python -m pip install -r requirements.txt
```

Using:

``` bash
python -m pip
```

helps ensure that packages are installed into the same Python
environment used to run FastAPI.

------------------------------------------------------------------------

## 5. Start the FastAPI Application

Run:

``` bash
python -m uvicorn main:app --reload
```

### What does `main:app` mean?

In:

``` text
main:app
```

`main` refers to:

``` text
main.py
```

and `app` refers to the FastAPI object:

``` python
app = FastAPI()
```

The command therefore tells Uvicorn:

``` text
Load the variable named app
from the Python module main.py
```

### What does `--reload` do?

``` text
--reload
```

tells the development server to restart automatically when source code
changes.

It is useful during development and classroom demonstrations.

------------------------------------------------------------------------

## 6. Open the Application

With Uvicorn running, open:

``` text
http://127.0.0.1:8000/
```

Keep the terminal running while testing the API.

To stop the server:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 7. Test the Example Endpoints

The example provides these URLs:

``` text
http://127.0.0.1:8000/
http://127.0.0.1:8000/course
http://127.0.0.1:8000/hello/Alex
http://127.0.0.1:8000/docs
```

You can enter these URLs directly into a browser because these examples
use GET requests.

------------------------------------------------------------------------

## 8. Root Endpoint

Open:

``` text
http://127.0.0.1:8000/
```

The request flow is:

``` text
Browser
   |
   | GET /
   v
FastAPI
   |
   v
Root path operation
   |
   v
Python return value
   |
   v
JSON response
   |
   v
Browser
```

------------------------------------------------------------------------

## 9. Course Endpoint

Open:

``` text
http://127.0.0.1:8000/course
```

This demonstrates a REST API endpoint that returns course information.

You can also test it from another terminal while Uvicorn remains
running:

``` bash
curl http://127.0.0.1:8000/course
```

FastAPI automatically serializes compatible Python data into JSON.

------------------------------------------------------------------------

## 10. Path Parameter Example

Open:

``` text
http://127.0.0.1:8000/hello/Alex
```

The value:

``` text
Alex
```

is part of the URL and is passed to the FastAPI path operation as a
**path parameter**.

Conceptually:

``` text
GET /hello/Alex
        |
        v
/hello/{name}
        |
        v
name = "Alex"
        |
        v
Python function
        |
        v
JSON response
```

Try changing the URL:

``` text
http://127.0.0.1:8000/hello/Sam
```

The path parameter changes from `Alex` to `Sam`.

------------------------------------------------------------------------

## 11. Typed Parameters

One important FastAPI feature is the use of Python type hints.

For example:

``` python
def example(score: int):
    ...
```

declares that:

``` text
score
```

is expected to be an integer.

FastAPI uses Python type information to help with:

-   request validation;
-   data conversion;
-   API documentation;
-   OpenAPI schema generation.

This is one reason FastAPI code often contains explicit type
annotations.

------------------------------------------------------------------------

## 12. Pydantic Validation

FastAPI integrates with **Pydantic** for structured data validation.

A Pydantic model can describe the expected structure of request data.

Conceptually:

``` text
Client JSON
    |
    v
Pydantic Model
    |
    +---- valid ----> Path Operation Function
    |
    +---- invalid --> Validation Error Response
```

This allows FastAPI to validate incoming data before the path operation
performs its main application logic.

The exact Pydantic models available in this example depend on the
definitions in `main.py`.

------------------------------------------------------------------------

## 13. Automatic API Documentation

FastAPI automatically generates OpenAPI documentation from the
application.

Open:

``` text
http://127.0.0.1:8000/docs
```

This displays the interactive **Swagger UI**.

Students can use it to:

-   view available endpoints;
-   inspect request parameters;
-   inspect response schemas;
-   expand individual operations;
-   execute API requests;
-   inspect returned status codes and responses.

The documentation is generated from the FastAPI application rather than
being manually written as a separate webpage.

------------------------------------------------------------------------

## 14. Testing with Swagger UI

Start the application:

``` bash
python -m uvicorn main:app --reload
```

Then open:

``` text
http://127.0.0.1:8000/docs
```

For an endpoint:

1.  Expand the endpoint.
2.  Select **Try it out**.
3.  Enter any required parameter values.
4.  Select **Execute**.
5.  Review the request URL.
6.  Review the response body.
7.  Review the HTTP status code.

This provides a convenient way to demonstrate API behavior without
requiring a separate API client.

------------------------------------------------------------------------

## 15. FastAPI vs. Flask in These Examples

The previous Flask example includes both an HTML webpage and API
endpoints.

This FastAPI example focuses primarily on building a typed REST API.

A simplified comparison is:

  -----------------------------------------------------------------------
  Concept                 Flask Basic             FastAPI Basic
  ----------------------- ----------------------- -----------------------
  Main focus              Web application + API   Typed REST API

  Application object      `Flask(__name__)`       `FastAPI()`

  Route decorator         `@app.route(...)`       `@app.get(...)`, etc.

  Type-driven validation  Usually added           Built into common
                          separately              FastAPI workflows

  JSON responses          Often `jsonify()`       Automatic for
                                                  compatible return
                                                  values

  Interactive API docs    Not automatic by        `/docs`
                          default                 

  OpenAPI generation      Not automatic by        Built in
                          default                 
  -----------------------------------------------------------------------

These are teaching distinctions for the examples in this repository;
both frameworks can support much more complex applications.

------------------------------------------------------------------------

## 16. Recommended Run Sequence

From inside `03-fastapi-basic`:

``` bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Then test:

``` text
http://127.0.0.1:8000/
http://127.0.0.1:8000/course
http://127.0.0.1:8000/hello/Alex
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

## 17. Troubleshooting: `No module named fastapi`

If you receive:

``` text
ModuleNotFoundError: No module named 'fastapi'
```

verify the active Python:

``` bash
which python
python --version
```

Check FastAPI:

``` bash
python -m pip show fastapi
```

If necessary:

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 18. Troubleshooting: `No module named uvicorn`

Check whether Uvicorn is installed:

``` bash
python -m pip show uvicorn
```

If it is missing:

``` bash
python -m pip install -r requirements.txt
```

Then retry:

``` bash
python -m uvicorn main:app --reload
```

------------------------------------------------------------------------

## 19. Troubleshooting: `Could not import module "main"`

If Uvicorn reports that it cannot import `main`, make sure you are
running the command from the directory containing:

``` text
main.py
```

On macOS/Linux:

``` bash
pwd
ls
```

You should see:

``` text
main.py
```

Then run:

``` bash
python -m uvicorn main:app --reload
```

------------------------------------------------------------------------

## 20. Troubleshooting: `Attribute "app" not found`

If you receive an error similar to:

``` text
Attribute "app" not found in module "main"
```

open `main.py` and confirm that it contains a FastAPI application object
named:

``` python
app = FastAPI()
```

The command:

``` bash
python -m uvicorn main:app --reload
```

expects:

``` text
main.py
   |
   └── app
```

If the FastAPI object has another variable name, the Uvicorn command
must use that variable name instead.

------------------------------------------------------------------------

## 21. Troubleshooting: Port 8000 Is Already in Use

If another application is already using port `8000`, either stop that
application or start Uvicorn on another port:

``` bash
python -m uvicorn main:app --reload --port 8001
```

Then open:

``` text
http://127.0.0.1:8001/
```

and:

``` text
http://127.0.0.1:8001/docs
```

------------------------------------------------------------------------

## 22. Quick Command Reference

  Goal                         Command
  ---------------------------- ---------------------------------------------
  Create virtual environment   `python3 -m venv .venv`
  Activate on macOS/Linux      `source .venv/bin/activate`
  Upgrade pip                  `python -m pip install --upgrade pip`
  Install dependencies         `python -m pip install -r requirements.txt`
  Check FastAPI                `python -m pip show fastapi`
  Check Uvicorn                `python -m pip show uvicorn`
  Start API                    `python -m uvicorn main:app --reload`
  Root endpoint                `http://127.0.0.1:8000/`
  Course endpoint              `http://127.0.0.1:8000/course`
  Path parameter example       `http://127.0.0.1:8000/hello/Alex`
  Swagger UI                   `http://127.0.0.1:8000/docs`
  Stop server                  `Ctrl+C`
  Leave virtual environment    `deactivate`

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Create and run a basic FastAPI application.
2.  Explain how a URL maps to a FastAPI path operation.
3.  Explain what `main:app` means in the Uvicorn command.
4.  Identify and use a path parameter.
5.  Explain why Python type hints are useful in FastAPI.
6.  Describe the role of Pydantic validation.
7.  Explain how FastAPI returns JSON responses.
8.  Use Swagger UI to inspect and execute API requests.
9.  Explain the role of automatic OpenAPI documentation.
10. Trace an HTTP request through a FastAPI application and back to the
    client.
