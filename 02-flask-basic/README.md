# 02 --- Flask Basic Example

This example demonstrates a basic Flask web application with both a
webpage and simple API endpoints.

It introduces three important Flask flows:

``` text
Browser → Route → View Function → Jinja Template → Browser
```

``` text
Client → GET API Endpoint → Python Logic → JSON Response
```

``` text
Client → POST API Endpoint → JSON Request → Python Logic → JSON Response
```

The example is intentionally small so students can focus on how Flask
handles routing, HTML templates, HTTP requests, and JSON responses.

------------------------------------------------------------------------

## 1. Project Structure

A simplified project structure is:

``` text
02-flask-basic/
├── app.py
├── requirements.txt
└── templates/
    └── home.html
```

The HTML file must be inside the directory named:

``` text
templates/
```

because Flask searches that directory for Jinja templates by default.

In this project, the webpage route uses:

``` python
render_template("home.html")
```

so the corresponding file is:

``` text
templates/home.html
```

------------------------------------------------------------------------

## 2. Application Architecture

### Webpage flow

``` text
Browser
   |
   | GET /
   v
Flask application
app.py
   |
   v
@app.route("/")
   |
   v
home()
   |
   v
render_template("home.html")
   |
   v
templates/home.html
   |
   | HTML response
   v
Browser
```

### GET API flow

``` text
Client
   |
   | GET /api/course
   v
Flask
   |
   v
get_course()
   |
   v
Python dictionary
   |
   v
jsonify(...)
   |
   v
JSON response
```

### POST API flow

``` text
Client
   |
   | POST /api/message
   | JSON: {"name": "Alex"}
   v
Flask
   |
   v
create_message()
   |
   v
request.get_json()
   |
   v
Python logic
   |
   v
jsonify(...)
   |
   v
JSON response + HTTP 201
```

------------------------------------------------------------------------

## 3. Create a Virtual Environment

From inside the `02-flask-basic` directory, create a Python virtual
environment:

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

On macOS/Linux, you can also run:

``` bash
which python
```

The path should point inside the `.venv` directory.

------------------------------------------------------------------------

## 4. Install the Dependencies

Upgrade pip:

``` bash
python -m pip install --upgrade pip
```

Install the packages listed in `requirements.txt`:

``` bash
python -m pip install -r requirements.txt
```

Using:

``` bash
python -m pip
```

helps ensure that packages are installed into the same Python
environment used to run the application.

------------------------------------------------------------------------

## 5. Start the Flask Application

In **Terminal 1**, make sure you are inside:

``` text
02-flask-basic/
```

and the virtual environment is active.

Run:

``` bash
python app.py
```

The Flask development server should start at approximately:

``` text
http://127.0.0.1:5000
```

Keep **Terminal 1 running** while testing the webpage and API endpoints.

To stop Flask later, use:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 6. Test the Webpage

Open a browser and go to:

``` text
http://127.0.0.1:5000/
```

The `/` route in `app.py` calls:

``` python
render_template("home.html")
```

Flask then loads:

``` text
templates/home.html
```

and returns the rendered HTML to the browser.

------------------------------------------------------------------------

## 7. Test the GET API Endpoint

Keep the Flask server running in **Terminal 1**.

Open **Terminal 2** and run:

``` bash
curl http://127.0.0.1:5000/api/course
```

The endpoint returns course information as JSON.

A response should look similar to:

``` json
{
  "course": "Web Framework Example",
  "framework": "Flask",
  "language": "Python"
}
```

### What happens?

The request:

``` text
GET /api/course
```

calls the Flask function:

``` text
get_course()
```

The function creates a Python dictionary and passes it to `jsonify()`.

Flask then returns the data as a JSON HTTP response.

------------------------------------------------------------------------

## 8. Test the POST API Endpoint

With Flask still running in **Terminal 1**, use **Terminal 2**:

``` bash
curl -X POST \
  http://127.0.0.1:5000/api/message \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex"}'
```

The client sends:

``` json
{
  "name": "Alex"
}
```

The Flask application reads the JSON request using:

``` python
request.get_json()
```

It then returns a JSON response similar to:

``` json
{
  "framework": "Flask",
  "message": "Hello, Alex!"
}
```

The endpoint returns HTTP status:

``` text
201 Created
```

------------------------------------------------------------------------

## 9. Understanding GET vs. POST

### GET

A GET request is normally used to retrieve information.

This example uses:

``` text
GET /api/course
```

The client sends a request and receives course information.

### POST

A POST request is commonly used when the client sends data to the
server.

This example uses:

``` text
POST /api/message
```

The client sends:

``` json
{
  "name": "Alex"
}
```

and the server uses that information to create its response.

------------------------------------------------------------------------

## 10. Understanding the Main Flask Components

### `Flask`

``` python
app = Flask(__name__)
```

creates the Flask application.

`__name__` helps Flask determine where the application is located so it
can find resources such as templates.

### `@app.route()`

A route connects a URL to a Python function.

For example:

``` python
@app.route("/")
```

connects the root URL `/` to the `home()` function.

### `render_template()`

`render_template()` loads an HTML template from the `templates/`
directory.

For this project:

``` python
render_template("home.html")
```

loads:

``` text
templates/home.html
```

### `jsonify()`

`jsonify()` converts Python data into a JSON HTTP response.

### `request`

The Flask `request` object provides access to information sent by the
client.

For the POST endpoint:

``` python
request.get_json()
```

reads JSON from the HTTP request body.

------------------------------------------------------------------------

## 11. Troubleshooting: `TemplateNotFound`

If you receive:

``` text
jinja2.exceptions.TemplateNotFound: home.html
```

check the project structure.

It should contain:

``` text
02-flask-basic/
├── app.py
└── templates/
    └── home.html
```

The folder name must be:

``` text
templates
```

not:

``` text
template
```

Also make sure `app.py` contains:

``` python
return render_template("home.html")
```

and not:

``` python
return render_template("index.html")
```

if the actual file is named `home.html`.

Do **not** write:

``` python
render_template("templates/home.html")
```

because Flask already searches inside the `templates/` directory.

------------------------------------------------------------------------

## 12. Troubleshooting: Flask Is Not Installed

If you receive an error such as:

``` text
ModuleNotFoundError: No module named 'flask'
```

verify the active environment:

``` bash
which python
python --version
```

Then check Flask:

``` bash
python -m pip show Flask
```

If necessary:

``` bash
python -m pip install -r requirements.txt
```

Then run:

``` bash
python app.py
```

------------------------------------------------------------------------

## 13. Troubleshooting: `curl` Cannot Connect

If `curl` reports that it cannot connect to:

``` text
127.0.0.1:5000
```

make sure the Flask server is still running in **Terminal 1**.

The workflow should be:

``` text
Terminal 1                         Terminal 2
----------                         ----------
python app.py
     |
     | Flask remains running
     |
     +---------------------------> curl GET request
     |
     +---------------------------> curl POST request
```

Do not stop the Flask server before running the API requests.

------------------------------------------------------------------------

## 14. Recommended Run Sequence

### Terminal 1 --- Start Flask

``` bash
cd 02-flask-basic

source .venv/bin/activate

python -m pip install -r requirements.txt

python app.py
```

Leave this terminal running.

### Browser --- Test the webpage

Open:

``` text
http://127.0.0.1:5000/
```

### Terminal 2 --- Test GET

``` bash
curl http://127.0.0.1:5000/api/course
```

### Terminal 2 --- Test POST

``` bash
curl -X POST \
  http://127.0.0.1:5000/api/message \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex"}'
```

------------------------------------------------------------------------

## 15. Quick Command Reference

  Goal                         Command
  ---------------------------- ---------------------------------------------
  Create virtual environment   `python3 -m venv .venv`
  Activate on macOS/Linux      `source .venv/bin/activate`
  Upgrade pip                  `python -m pip install --upgrade pip`
  Install dependencies         `python -m pip install -r requirements.txt`
  Start Flask                  `python app.py`
  Open webpage                 `http://127.0.0.1:5000/`
  Test GET API                 `curl http://127.0.0.1:5000/api/course`
  Stop Flask                   `Ctrl+C`
  Leave virtual environment    `deactivate`

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain how a Flask route connects a URL to a Python view function.
2.  Explain how Flask renders a Jinja HTML template.
3.  Identify why HTML templates are stored in the `templates/`
    directory.
4.  Explain the difference between a webpage route and an API endpoint.
5.  Explain the basic difference between GET and POST requests.
6.  Return JSON from a Flask API using `jsonify()`.
7.  Read JSON request data using `request.get_json()`.
8.  Test API endpoints using `curl`.
9.  Trace webpage and API requests through a Flask application.
