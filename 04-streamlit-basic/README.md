# 04 --- Streamlit Basic Example

This example demonstrates a **Python-first reactive user interface**
using Streamlit.

Unlike the previous Flask example, students do not need to write HTML
templates or JavaScript to create the basic interface. Streamlit
converts Python commands and widgets into an interactive web
application.

The example introduces:

-   Streamlit application structure;
-   Python-based UI components;
-   interactive widgets;
-   reactive application execution;
-   user input and displayed output;
-   running a Streamlit development server.

------------------------------------------------------------------------

## 1. Basic Architecture

A simplified Streamlit flow is:

``` text
Browser
   |
   | User opens the application
   v
Streamlit Server
   |
   v
app.py
   |
   | Python executes
   v
Streamlit UI Components
   |
   v
Browser
```

When the user interacts with a widget, Streamlit normally reruns the
Python script:

``` text
User changes a widget
        |
        v
Streamlit detects interaction
        |
        v
app.py reruns
        |
        v
Current widget values are read
        |
        v
UI is updated
        |
        v
Browser displays new result
```

This reactive execution model is an important difference between
Streamlit and traditional route-based web frameworks.

------------------------------------------------------------------------

## 2. Project Structure

A basic structure is:

``` text
04-streamlit-basic/
├── app.py
├── requirements.txt
└── README.md
```

The main application is:

``` text
app.py
```

For this simple example, Streamlit does not require:

``` text
templates/
static/
```

directories.

The user interface can be defined directly in Python.

------------------------------------------------------------------------

## 3. Create a Virtual Environment

From inside the `04-streamlit-basic` directory:

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

The Python path should point inside `.venv`.

------------------------------------------------------------------------

## 4. Install the Dependencies

Upgrade pip:

``` bash
python -m pip install --upgrade pip
```

Install the packages in `requirements.txt`:

``` bash
python -m pip install -r requirements.txt
```

Using:

``` bash
python -m pip
```

helps ensure packages are installed into the same Python environment
used to run the application.

Verify Streamlit:

``` bash
python -m pip show streamlit
```

You can also check the installed Streamlit version:

``` bash
python -m streamlit version
```

------------------------------------------------------------------------

## 5. Start the Streamlit Application

Run:

``` bash
python -m streamlit run app.py
```

Streamlit should display information similar to:

``` text
Local URL: http://localhost:8501
```

Open:

``` text
http://localhost:8501
```

in your browser.

Keep the terminal running while using the application.

To stop Streamlit:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 6. Why Use `python -m streamlit`?

You may also see:

``` bash
streamlit run app.py
```

However, this repository uses:

``` bash
python -m streamlit run app.py
```

because it explicitly runs Streamlit using the currently active Python
interpreter.

This is useful when working with virtual environments because it reduces
confusion about which Streamlit installation is being used.

------------------------------------------------------------------------

## 7. Understanding a Streamlit Application

A Streamlit application is a Python script.

For example, an application may contain:

``` python
import streamlit as st

st.title("Student Score")

score = st.number_input(
    "Enter a score",
    min_value=0,
    max_value=100,
    value=70
)

if st.button("Evaluate"):
    if score >= 70:
        st.success("Pass")
    else:
        st.warning("Needs Improvement")
```

This example contains:

``` text
st.title()
```

to display a title,

``` text
st.number_input()
```

to collect numeric input,

``` text
st.button()
```

to respond to a user action, and

``` text
st.success()
st.warning()
```

to display results.

------------------------------------------------------------------------

## 8. Understanding Reactive Execution

A traditional web framework often maps URLs to route functions.

Streamlit behaves differently.

When Streamlit first loads:

``` text
app.py
  |
  v
Python executes from top to bottom
  |
  v
Widgets are created
  |
  v
UI appears in browser
```

When a user changes a widget or clicks a button:

``` text
User interaction
      |
      v
Streamlit reruns app.py
      |
      v
Widget state is available
      |
      v
Python conditions execute
      |
      v
Updated UI is displayed
```

This is why Streamlit is often convenient for:

-   data applications;
-   machine-learning demonstrations;
-   dashboards;
-   prototypes;
-   interactive analytics tools.

------------------------------------------------------------------------

## 9. Widgets

Streamlit provides Python functions for common interface components.

Examples include:

``` python
st.text_input("Name")
```

``` python
st.number_input("Score")
```

``` python
st.selectbox("Choose an option", ["A", "B", "C"])
```

``` python
st.button("Submit")
```

``` python
st.slider("Value", 0, 100)
```

Widgets return values that can be used directly in Python code.

Conceptually:

``` text
Widget
   |
   v
Python value
   |
   v
Application logic
   |
   v
Streamlit output
```

------------------------------------------------------------------------

## 10. Displaying Output

Streamlit also provides functions for displaying different types of
information.

Examples include:

``` python
st.write("Hello")
```

``` python
st.success("Operation completed")
```

``` python
st.warning("Check this value")
```

``` python
st.error("An error occurred")
```

``` python
st.info("Additional information")
```

These functions allow Python code to control what the user sees in the
browser.

------------------------------------------------------------------------

## 11. Streamlit Compared with Flask and FastAPI

The examples in this repository demonstrate different framework
purposes.

  -----------------------------------------------------------------------
  Concept           Flask Basic       FastAPI Basic     Streamlit Basic
  ----------------- ----------------- ----------------- -----------------
  Primary teaching  Web app + API     Typed REST API    Interactive
  focus                                                 Python UI

  Main file         `app.py`          `main.py`         `app.py`

  HTML required for Yes               No                No
  basic example                                         

  Route-based       Yes               Yes               Not in the same
                                                        style

  Interactive       Requires frontend Requires          Built in
  widgets           work              frontend/client   

  JSON API focus    Supported         Primary strength  Not primary focus

  Automatic API     No by default     Yes               Not applicable
  docs                                                  

  Typical local     `5000`            `8000`            `8501`
  port                                                  
  -----------------------------------------------------------------------

These are simplified distinctions for the teaching examples. Each
framework supports capabilities beyond what is demonstrated here.

------------------------------------------------------------------------

## 12. Recommended Run Sequence

From inside `04-streamlit-basic`:

``` bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m streamlit run app.py
```

Then open:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

## 13. Troubleshooting: `No module named streamlit`

If you receive:

``` text
ModuleNotFoundError: No module named 'streamlit'
```

verify the active Python:

``` bash
which python
python --version
```

Check whether Streamlit is installed:

``` bash
python -m pip show streamlit
```

If necessary:

``` bash
python -m pip install -r requirements.txt
```

Then retry:

``` bash
python -m streamlit run app.py
```

------------------------------------------------------------------------

## 14. Troubleshooting: `streamlit: command not found`

If:

``` bash
streamlit run app.py
```

produces:

``` text
command not found: streamlit
```

first activate the virtual environment:

``` bash
source .venv/bin/activate
```

Then use:

``` bash
python -m streamlit run app.py
```

This explicitly uses Streamlit from the active Python environment.

------------------------------------------------------------------------

## 15. Troubleshooting: `app.py` Cannot Be Found

Make sure you are running the command from the directory containing:

``` text
app.py
```

Check the current location:

``` bash
pwd
```

List the files:

``` bash
ls
```

You should see:

``` text
app.py
```

Then run:

``` bash
python -m streamlit run app.py
```

------------------------------------------------------------------------

## 16. Troubleshooting: Port 8501 Is Already in Use

If another Streamlit application is already running, stop it with:

``` text
Ctrl+C
```

or run this application on another port:

``` bash
python -m streamlit run app.py --server.port 8502
```

Then open:

``` text
http://localhost:8502
```

------------------------------------------------------------------------

## 17. Troubleshooting: Browser Does Not Open Automatically

Streamlit may not always open the browser automatically.

If the terminal shows:

``` text
Local URL: http://localhost:8501
```

manually open:

``` text
http://localhost:8501
```

in your browser.

The terminal running Streamlit must remain open.

------------------------------------------------------------------------

## 18. Important: Do Not Run a Streamlit App with Plain Python

For a normal Streamlit application, do not start it with:

``` bash
python app.py
```

Instead use:

``` bash
python -m streamlit run app.py
```

Streamlit needs its application runner to create the web server, manage
widgets, and handle reactive reruns.

------------------------------------------------------------------------

## 19. Quick Command Reference

  -----------------------------------------------------------------------------------------
  Goal                                Command
  ----------------------------------- -----------------------------------------------------
  Create virtual environment          `python3 -m venv .venv`

  Activate on macOS/Linux             `source .venv/bin/activate`

  Upgrade pip                         `python -m pip install --upgrade pip`

  Install dependencies                `python -m pip install -r requirements.txt`

  Check Streamlit                     `python -m pip show streamlit`

  Start application                   `python -m streamlit run app.py`

  Open application                    `http://localhost:8501`

  Run on port 8502                    `python -m streamlit run app.py --server.port 8502`

  Stop application                    `Ctrl+C`

  Leave virtual environment           `deactivate`
  -----------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain what Streamlit is used for.
2.  Create and run a basic Streamlit application.
3.  Explain why a basic Streamlit UI does not require HTML or
    JavaScript.
4.  Identify common Streamlit widgets.
5.  Use widget values in Python application logic.
6.  Explain Streamlit's reactive rerun model.
7.  Explain why `python -m streamlit run app.py` is used instead of
    `python app.py`.
8.  Identify the differences among the basic Flask, FastAPI, and
    Streamlit examples.
9.  Trace a user interaction through the Streamlit application and back
    to the browser.
