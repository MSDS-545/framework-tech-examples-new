# Teaching Guide

## What students should compare

### Django
Django is a larger Python web framework. The basic example emphasizes project configuration, application routing, views, and server-rendered templates. Introduce models/ORM later.

### Flask
Flask starts with a smaller core. Compare `@app.route()` directly with Django's separate URL configuration.

### FastAPI
FastAPI is particularly useful for APIs. Point out type annotations, Pydantic validation, JSON responses, and `/docs`.

### Streamlit
Streamlit lets Python code define a data-oriented web interface. Explain that user interactions cause the script to rerun.

### Vue
Vue runs in the browser. Explain `index.html → main.js → App.vue`, reactive `ref()` state, templates, and events.

### React
React also runs primarily in the browser. Compare JSX and `useState()` with Vue's template and `ref()` model.

### Node.js
Node.js is the JavaScript runtime. The built-in HTTP example deliberately avoids Express so students can see the distinction.

### Express.js
Express runs on Node.js and adds routing/middleware conveniences. Compare the low-level Node server with the shorter Express server.

### PostgreSQL
PostgreSQL is a database, not a web framework. Keep the first lesson focused on tables, constraints, SQL, and persistence before connecting it to an application ORM.

### FastAPI + Streamlit
Use the final example to introduce service separation and HTTP communication: the UI does not import and call the API function directly; it sends a network request.

## Suggested live sequence

1. Run each basic example unchanged.
2. Identify the entry point.
3. Trace one browser request through the framework.
4. Change one displayed message.
5. Add one new route or interaction.
6. Compare where state/data lives.
7. Only after these basics, introduce a larger CRUD or database-backed application.
