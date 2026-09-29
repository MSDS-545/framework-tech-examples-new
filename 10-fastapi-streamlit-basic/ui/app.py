import requests
import streamlit as st

# ---------------------------------------------------------
# STREAMLIT USER INTERFACE
# ---------------------------------------------------------

st.title("FastAPI + Streamlit Example")

# Let the user enter a name.
name = st.text_input(
    "Enter your name:",
    value="Student"
)


# ---------------------------------------------------------
# FASTAPI CONNECTION
# ---------------------------------------------------------

# Address of our FastAPI backend.
API_URL = "http://127.0.0.1:8000"


if st.button("Get Greeting"):

    try:
        # Send the name to FastAPI as a query parameter.
        #
        # requests converts:
        # {"name": "Student"}
        #
        # into:
        # ?name=Student
        response = requests.get(
            f"{API_URL}/api/greeting",
            params={"name": name}
        )

        # Raise an error if FastAPI returns
        # something such as 404 or 500.
        response.raise_for_status()

        # Convert FastAPI's JSON response
        # into a Python dictionary.
        data = response.json()

        # Display the result in Streamlit.
        st.success(data["message"])

    except requests.RequestException as error:

        st.error(
            f"Could not reach the API: {error}"
        )