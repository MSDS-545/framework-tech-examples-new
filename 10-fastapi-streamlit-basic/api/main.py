from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI(
    title="FastAPI + Streamlit Basic Example"
)


@app.get("/")
def root():
    """
    Simple root route used to verify that
    the FastAPI server is running.
    """
    return {
        "message": "FastAPI is running"
    }


@app.get("/api/greeting")
def greeting(name: str = "Student"):
    """
    Return a greeting to the Streamlit application.

    The 'name' value is received as a query parameter.

    Example:
    /api/greeting?name=Student
    """

    return {
        "message": f"Hello, {name}!"
    }