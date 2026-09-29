# Framework & Technology Examples

A collection of small, independent teaching examples for introducing modern web frameworks and supporting technologies. The examples intentionally **do not use a shared Task application**. Each project demonstrates the framework itself with a simple message, interaction, API response, or database operation.

## Examples

| Folder | Technology | Main concept | Default port |
|---|---|---|---|
| `01-django-basic` | Django | Project/app, URL → View → Template | 8000 |
| `02-flask-basic` | Flask | Route → Template | 5000 |
| `03-fastapi-basic` | FastAPI | Typed REST API + OpenAPI | 8000 |
| `04-streamlit-basic` | Streamlit | Reactive Python UI | 8501 |
| `05-vue-basic` | Vue + Vite | Reactive state + component | 5173 |
| `06-react-basic` | React + Vite | Component + state | 5173 |
| `07-node-basic` | Node.js | JavaScript server runtime | 3000 |
| `08-express-basic` | Express.js | Routes + middleware | 3000 |
| `09-postgresql-basic` | PostgreSQL | SQL schema + CRUD | 5432 |
| `10-fastapi-streamlit-basic` | FastAPI + Streamlit | Separate API and UI | 8000/8501 |

## Prerequisites

- VS Code
- Git
- Python 3.11+
- Node.js 20+ and npm
- PostgreSQL 16+ for the PostgreSQL example
- Docker Desktop is optional; `09-postgresql-basic` includes Docker Compose.

## Recommended teaching order

Start with Django and Flask to show server-rendered Python web applications. Then introduce FastAPI and REST APIs, Streamlit as a Python-first UI, Vue and React as browser frontend frameworks, Node.js as a JavaScript runtime, Express as a Node web framework, and PostgreSQL for persistent relational data.

## Important distinction

`Node.js` is a JavaScript **runtime**. `Express.js` is a web **framework/library that runs on Node.js**. Vue and React primarily build browser interfaces. Django, Flask, FastAPI, and Express process server-side requests. PostgreSQL stores persistent data.

## Running examples

Every folder has its own `README.md`. Run commands from that example's folder. Python examples use a local `.venv`; JavaScript examples use their own `package.json` and `node_modules`.

## Comments

Source files are intentionally commented for instruction. Comments focus on framework concepts, request flow, configuration, and why important lines exist rather than commenting trivial syntax.
