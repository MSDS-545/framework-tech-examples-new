# 01 --- Django Basic Example

Demonstrates Django's basic **URL → View → Template → Browser** flow
without creating a custom database model.

The purpose of this example is to introduce the main Django project
structure and show how a browser request moves through Django before an
HTML page is returned.

## Architecture

``` text
Browser
   ↓
config/urls.py
   ↓
demo/urls.py
   ↓
demo/views.py
   ↓
templates/home.html
   ↓
Browser
```

-   `config/` contains the Django **project configuration**.
-   `demo/` is the Django **application** used to demonstrate routing,
    views, and templates.
-   `templates/` contains the HTML templates rendered by Django views.
-   `manage.py` is Django's command-line utility for working with the
    project.

A simplified structure is:

``` text
01-django-basic/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
├── demo/
│   ├── urls.py
│   └── views.py
└── templates/
    └── home.html
```

## 1. Create the Virtual Environment

For this teaching example, use Python 3.11 when available.

Check Python:

``` bash
python3.11 --version
```

Create the environment:

``` bash
python3.11 -m venv .venv
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

The path should point to `.venv`.

## 2. Install Dependencies

Upgrade pip:

``` bash
python -m pip install --upgrade pip
```

Install the project requirements:

``` bash
python -m pip install -r requirements.txt
```

Using `python -m pip` helps ensure packages are installed into the
Python environment currently being used.

## 3. Verify Django

``` bash
python -m django --version
```

You can also verify the import:

``` bash
python -c "import django; print(django.get_version())"
```

Or inspect the installed package:

``` bash
python -m pip show Django
```

## 4. Check and Initialize the Project

Check the Django configuration:

``` bash
python manage.py check
```

This basic example does not define a custom database model, so students
normally do not need to create custom migrations.

Django's built-in applications still use database tables. Initialize
them with:

``` bash
python manage.py migrate
```

## 5. Run Django

``` bash
python manage.py runserver
```

Open:

``` text
http://127.0.0.1:8000/
```

Stop the development server with:

``` text
Ctrl+C
```

## Recommended Setup Sequence

For a fresh setup on macOS/Linux:

``` bash
python3.11 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m django --version
python manage.py check
python manage.py migrate
python manage.py runserver
```

Students should not run the troubleshooting commands below unless the
normal setup fails.

## Understanding the Django Request Flow

When the browser requests `http://127.0.0.1:8000/`, the request moves
through the project as follows:

``` text
Browser
   |
   | HTTP GET /
   v
config/urls.py
   |
   | Project-level routing
   v
demo/urls.py
   |
   | Application-level routing
   v
demo/views.py
   |
   | View function
   v
render(...)
   |
   v
templates/home.html
   |
   | HTML response
   v
Browser
```

### `config/urls.py`

This is the project-level URL configuration. It determines which Django
application should receive a request.

### `demo/urls.py`

This file defines routes for the `demo` application.

### `demo/views.py`

The view contains Python code that handles the request. A webpage view
can render an HTML template.

### `templates/home.html`

This is the HTML template returned to the browser.

## Troubleshooting: Confirm the Active Environment

If Django cannot be imported or the application does not start:

``` bash
which python
python --version
python -m pip --version
python -m pip show Django
```

The Python and pip paths should normally point inside `.venv`.

If necessary, activate the environment again:

``` bash
source .venv/bin/activate
```

## Troubleshooting: `No module named django`

Check the active Python:

``` bash
which python
python --version
```

Check whether Django is installed:

``` bash
python -m pip show Django
```

If it is missing:

``` bash
python -m pip install -r requirements.txt
```

Verify:

``` bash
python -c "import django; print(django.get_version())"
```

## Troubleshooting: Rebuild the Virtual Environment

If the virtual environment was created with the wrong Python version or
has become inconsistent, rebuild only `.venv`.

``` bash
deactivate
rm -rf .venv

python3.11 -m venv .venv
source .venv/bin/activate

python --version

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -c "import django; print(django.get_version())"

python manage.py check
python manage.py migrate
python manage.py runserver
```

Deleting `.venv` does **not** delete the Django project.

## Troubleshooting: Package Installation Problems

Inspect pip configuration:

``` bash
python -m pip config list
```

If necessary, Django can be installed directly from PyPI:

``` bash
python -m pip install Django --index-url https://pypi.org/simple
```

For the normal course workflow, prefer:

``` bash
python -m pip install -r requirements.txt
```

so students install the dependencies specified by the project.

## Common Mistakes

### Running commands outside the project directory

Before running:

``` bash
python manage.py runserver
```

make sure the current directory contains `manage.py`.

On macOS/Linux:

``` bash
ls
```

### Forgetting to activate the virtual environment

``` bash
source .venv/bin/activate
```

### Installing packages into a different Python environment

Prefer:

``` bash
python -m pip install -r requirements.txt
```

instead of relying on a potentially different `pip` executable.

### Creating another Django project unnecessarily

If `manage.py`, `config/`, and `demo/` already exist, do not run
`django-admin startproject` again. The repository already contains the
project students are supposed to run.

## Quick Command Reference

  Goal                             Command
  -------------------------------- ---------------------------------------------
  Create Python 3.11 environment   `python3.11 -m venv .venv`
  Activate on macOS/Linux          `source .venv/bin/activate`
  Check Python                     `python --version`
  Upgrade pip                      `python -m pip install --upgrade pip`
  Install dependencies             `python -m pip install -r requirements.txt`
  Check Django version             `python -m django --version`
  Check project                    `python manage.py check`
  Initialize Django tables         `python manage.py migrate`
  Start server                     `python manage.py runserver`
  Stop server                      `Ctrl+C`
  Leave environment                `deactivate`

## Learning Outcomes

After completing this example, students should be able to:

1.  Identify the difference between a Django **project** and a Django
    **application**.
2.  Explain project-level and application-level URL routing.
3.  Explain how a URL is connected to a Django view.
4.  Explain how a view renders an HTML template.
5.  Create and activate a Python virtual environment.
6.  Install Django project dependencies.
7.  Run a basic Django application locally.
8.  Trace a browser request through Django and back to the browser.
