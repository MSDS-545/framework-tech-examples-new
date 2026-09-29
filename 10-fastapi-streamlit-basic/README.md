# 10 --- FastAPI + Streamlit Basic Integration

This example demonstrates how **two separate Python services** can work
together:

-   **FastAPI** provides the backend API.
-   **Streamlit** provides the user interface.
-   Streamlit sends an HTTP request to FastAPI.
-   FastAPI returns JSON.
-   Streamlit displays the result to the user.

There is **no database** and **no Task model** in this example.

The purpose is to teach the service-to-service integration clearly
before adding databases, authentication, or more complex application
architecture.

------------------------------------------------------------------------

## 1. Overall Architecture

``` text
Browser
   |
   v
Streamlit UI
localhost:8501
   |
   | HTTP GET
   v
FastAPI API
127.0.0.1:8000
   |
   | JSON Response
   v
Streamlit UI
   |
   v
Browser
```

The complete flow is:

``` text
Browser
   |
   v
Streamlit
   |
   | GET /api/greeting?name=Student
   v
FastAPI
   |
   | Process request
   v
JSON
   |
   v
Streamlit
   |
   | Display response
   v
Browser
```

This is an important architectural distinction:

> Streamlit does not call a Python function inside the FastAPI
> application directly. It communicates with FastAPI over HTTP.

------------------------------------------------------------------------

## 2. Project Structure

Based on the commands used by this example, the important structure is:

``` text
fastapi-streamlit-basic/
├── requirements.txt
├── api/
│   ├── __init__.py
│   └── main.py
└── ui/
    ├── __init__.py
    └── app.py
```

The two important application files are:

``` text
api/main.py
ui/app.py
```

### `api/main.py`

Contains the FastAPI backend.

### `ui/app.py`

Contains the Streamlit user interface.

Because these are separate services, **both must be running at the same
time**.

------------------------------------------------------------------------

# Part A --- Environment Setup

## 3. Open the Project Directory

In a terminal:

``` bash
cd fastapi-streamlit-basic
```

Verify your location:

``` bash
pwd
ls
```

You should be in the directory containing:

``` text
requirements.txt
api/
ui/
```

------------------------------------------------------------------------

## 4. Create the Virtual Environment

Create the environment once:

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

------------------------------------------------------------------------

## 5. Install the Dependencies

With the virtual environment active:

``` bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Using:

``` bash
python -m pip
```

helps ensure the packages are installed into the same Python environment
being used to run the applications.

------------------------------------------------------------------------

# Part B --- Start FastAPI

## 6. Terminal 1 --- Start the Backend

Open **Terminal 1**.

Navigate to the project:

``` bash
cd fastapi-streamlit-basic
```

Activate the virtual environment:

``` bash
source .venv/bin/activate
```

Start FastAPI:

``` bash
python -m uvicorn api.main:app --reload --port 8000
```

Leave Terminal 1 running.

### What does `api.main:app` mean?

``` text
api.main
```

means:

``` text
api/main.py
```

and:

``` text
app
```

refers to the FastAPI application object inside that file.

Conceptually:

``` text
api/main.py
    |
    v
app = FastAPI()
    |
    v
Uvicorn
    |
    v
Port 8000
```

------------------------------------------------------------------------

## 7. Verify FastAPI Before Starting Streamlit

Before adding the UI, verify that the API works independently.

Open:

``` text
http://127.0.0.1:8000/docs
```

This opens FastAPI's Swagger UI.

The example includes:

``` text
GET /api/greeting
```

Test directly in a browser:

``` text
http://127.0.0.1:8000/api/greeting?name=Student
```

You can also try:

``` text
http://127.0.0.1:8000/api/greeting?name=Asmah
```

The API should return JSON.

This checkpoint is useful because it separates:

``` text
Is FastAPI working?
```

from:

``` text
Is Streamlit communicating with FastAPI?
```

------------------------------------------------------------------------

## 8. Test the API with `curl`

With FastAPI still running in Terminal 1, use another terminal:

``` bash
curl "http://127.0.0.1:8000/api/greeting?name=Student"
```

The flow is:

``` text
curl
  |
  | HTTP GET
  v
FastAPI
  |
  v
/api/greeting
  |
  v
JSON response
```

------------------------------------------------------------------------

# Part C --- Start Streamlit

## 9. Terminal 2 --- Start the User Interface

Open **Terminal 2**.

Navigate to the same project:

``` bash
cd fastapi-streamlit-basic
```

Activate the same virtual environment:

``` bash
source .venv/bin/activate
```

Start Streamlit:

``` bash
python -m streamlit run ui/app.py
```

Leave Terminal 2 running.

Open:

``` text
http://localhost:8501
```

You should now have:

``` text
Terminal 1
FastAPI
http://127.0.0.1:8000
```

and:

``` text
Terminal 2
Streamlit
http://localhost:8501
```

running simultaneously.

------------------------------------------------------------------------

# Part D --- Understand the Integration

## 10. What Happens When the User Uses the Streamlit UI?

The interaction follows this sequence:

``` text
1. User opens Streamlit
            |
            v
2. Streamlit displays the UI
            |
            v
3. User provides/selects a name
            |
            v
4. Streamlit sends an HTTP GET request
            |
            v
5. FastAPI receives /api/greeting
            |
            v
6. FastAPI returns JSON
            |
            v
7. Streamlit reads the JSON
            |
            v
8. Streamlit displays the result
```

This is a small example of a **frontend/backend service architecture**.

------------------------------------------------------------------------

## 11. Why Use Two Terminals?

Both applications are servers.

FastAPI needs its own running process:

``` text
Terminal 1
    |
    v
Uvicorn
    |
    v
FastAPI
```

Streamlit needs another running process:

``` text
Terminal 2
    |
    v
Streamlit Server
    |
    v
Streamlit UI
```

If either process stops, part of the application stops working.

------------------------------------------------------------------------

## 12. Ports

The two applications use different ports.

  Service        Address
  -------------- ------------------------------
  FastAPI        `http://127.0.0.1:8000`
  FastAPI docs   `http://127.0.0.1:8000/docs`
  Streamlit      `http://localhost:8501`

A port helps the operating system distinguish between different network
services running on the same computer.

Conceptually:

``` text
Computer
   |
   +---- Port 8000 ---- FastAPI
   |
   +---- Port 8501 ---- Streamlit
```

------------------------------------------------------------------------

## 13. The Greeting API

The backend endpoint is:

``` text
GET /api/greeting
```

A request can include the query parameter:

``` text
name
```

For example:

``` text
/api/greeting?name=Student
```

Conceptually:

``` text
/api/greeting?name=Student
               |
               v
          name = Student
               |
               v
         FastAPI logic
               |
               v
          JSON response
```

------------------------------------------------------------------------

## 14. Query Parameter vs. Path Parameter

This example uses a **query parameter**:

``` text
/api/greeting?name=Student
```

The parameter appears after:

``` text
?
```

This differs from a path parameter such as:

``` text
/hello/Student
```

A simplified comparison is:

  Type              Example
  ----------------- ------------------------------
  Query parameter   `/api/greeting?name=Student`
  Path parameter    `/hello/Student`

------------------------------------------------------------------------

## 15. JSON as the Service Boundary

FastAPI returns data to Streamlit as JSON.

Conceptually:

``` text
FastAPI Python
      |
      v
JSON Response
      |
      | HTTP
      v
Streamlit Python
      |
      v
Displayed UI
```

The two services do not need to share the same Python function call.

They communicate through the API contract.

------------------------------------------------------------------------

# Part E --- Recommended Run Sequence

## 16. One-Time Setup

From the project directory:

``` bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 17. Every Time You Run the Project

### Terminal 1 --- FastAPI

``` bash
cd fastapi-streamlit-basic
source .venv/bin/activate
python -m uvicorn api.main:app --reload --port 8000
```

Verify:

``` text
http://127.0.0.1:8000/docs
```

and:

``` text
http://127.0.0.1:8000/api/greeting?name=Student
```

### Terminal 2 --- Streamlit

``` bash
cd fastapi-streamlit-basic
source .venv/bin/activate
python -m streamlit run ui/app.py
```

Open:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

# Part F --- Troubleshooting

## 18. FastAPI Returns `404 Not Found`

If:

``` text
http://127.0.0.1:8000/api/greeting?name=Student
```

returns:

``` text
404 Not Found
```

first open:

``` text
http://127.0.0.1:8000/docs
```

Check whether:

``` text
GET /api/greeting
```

appears in the API documentation.

You can also inspect route decorators in the source:

``` bash
grep -n "@app" api/main.py
```

This can help confirm which routes are actually defined.

------------------------------------------------------------------------

## 19. Wrong Uvicorn Import Path

For this project, use:

``` bash
python -m uvicorn api.main:app --reload --port 8000
```

Do **not** use:

``` bash
python -m uvicorn main:app --reload
```

unless there is actually a `main.py` in the current project root
containing the FastAPI `app`.

The project structure used here places the FastAPI file at:

``` text
api/main.py
```

Therefore:

``` text
api.main:app
```

is the appropriate import path.

------------------------------------------------------------------------

## 20. `Could not import module "api.main"`

Check your current directory:

``` bash
pwd
ls
```

You should be at the project root where both of these are visible:

``` text
api/
ui/
```

Then retry:

``` bash
python -m uvicorn api.main:app --reload --port 8000
```

------------------------------------------------------------------------

## 21. Streamlit Opens but the API Call Fails

If the Streamlit page opens but cannot retrieve the greeting:

1.  Confirm Terminal 1 is still running FastAPI.
2.  Open:

``` text
http://127.0.0.1:8000/docs
```

3.  Test:

``` text
http://127.0.0.1:8000/api/greeting?name=Student
```

4.  If the direct API request fails, fix FastAPI first.
5.  If the direct API request works, inspect the URL used by the
    Streamlit code.

The Streamlit application should call the FastAPI service at the correct
host, port, and route.

------------------------------------------------------------------------

## 22. `No module named fastapi`

Activate the environment:

``` bash
source .venv/bin/activate
```

Then check:

``` bash
python -m pip show fastapi
```

If needed:

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 23. `No module named streamlit`

Activate the environment:

``` bash
source .venv/bin/activate
```

Check:

``` bash
python -m pip show streamlit
```

If needed:

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 24. Port 8000 Is Already in Use

If FastAPI cannot use port `8000`, first check whether another
Uvicorn/FastAPI process is already running.

Stop the old process with:

``` text
Ctrl+C
```

If necessary, FastAPI can run on another port:

``` bash
python -m uvicorn api.main:app --reload --port 8001
```

However, if Streamlit is configured to call port `8000`, its API URL
must also be changed to port `8001`.

This demonstrates an important integration concept:

> The frontend must know the correct backend address.

------------------------------------------------------------------------

## 25. Port 8501 Is Already in Use

Run Streamlit on another port:

``` bash
python -m streamlit run ui/app.py --server.port 8502
```

Then open:

``` text
http://localhost:8502
```

Changing the Streamlit port does not necessarily require changing
FastAPI because the backend remains a separate service.

------------------------------------------------------------------------

# Part G --- Stopping the Project

## 26. Stop FastAPI

Go to Terminal 1 and press:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 27. Stop Streamlit

Go to Terminal 2 and press:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 28. Leave the Virtual Environment

After both services are stopped, run:

``` bash
deactivate
```

------------------------------------------------------------------------

# Part H --- Quick Reference

## 29. Command Table

  -------------------------------------------------------------------------------------------------------
  Location                Goal                    Command
  ----------------------- ----------------------- -------------------------------------------------------
  Project root            Create venv             `python3 -m venv .venv`

  Terminal                Activate venv           `source .venv/bin/activate`

  Project root            Install dependencies    `python -m pip install -r requirements.txt`

  Terminal 1              Start FastAPI           `python -m uvicorn api.main:app --reload --port 8000`

  Browser                 FastAPI docs            `http://127.0.0.1:8000/docs`

  Browser                 Test greeting API       `http://127.0.0.1:8000/api/greeting?name=Student`

  Terminal 2              Start Streamlit         `python -m streamlit run ui/app.py`

  Browser                 Open Streamlit          `http://localhost:8501`

  Either server terminal  Stop service            `Ctrl+C`

  Terminal                Leave venv              `deactivate`
  -------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 30. Architecture Summary

``` text
                  TWO RUNNING SERVICES

             ┌─────────────────────┐
             │       Browser       │
             └──────────┬──────────┘
                        │
                        v
             ┌─────────────────────┐
             │    Streamlit UI     │
             │   localhost:8501    │
             └──────────┬──────────┘
                        │
                        │ HTTP GET
                        │ /api/greeting?name=...
                        v
             ┌─────────────────────┐
             │      FastAPI        │
             │ 127.0.0.1:8000     │
             └──────────┬──────────┘
                        │
                        │ JSON
                        v
             ┌─────────────────────┐
             │    Streamlit UI     │
             └──────────┬──────────┘
                        │
                        v
             ┌─────────────────────┐
             │       Browser       │
             └─────────────────────┘
```

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain why FastAPI and Streamlit run as two separate services.
2.  Start FastAPI and Streamlit in separate terminals.
3.  Explain the role of Uvicorn in the FastAPI service.
4.  Explain why the Uvicorn import path is `api.main:app`.
5.  Test a FastAPI endpoint independently before connecting a frontend.
6.  Use FastAPI Swagger documentation at `/docs`.
7.  Explain the difference between a query parameter and a path
    parameter.
8.  Explain how Streamlit communicates with FastAPI over HTTP.
9.  Explain the role of JSON between the two services.
10. Explain why FastAPI and Streamlit use different ports.
11. Troubleshoot a `404 Not Found` response by checking the FastAPI
    routes.
12. Trace the complete request flow from browser → Streamlit → FastAPI →
    JSON → Streamlit → browser.
