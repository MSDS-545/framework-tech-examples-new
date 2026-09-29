# 08 --- Express.js Basic Example

This example demonstrates a basic **Express.js web application running
on Node.js**.

The most important relationship in this example is:

``` text
Node.js
   |
   v
Express.js
   |
   v
Web Application / API
```

Node.js provides the JavaScript runtime. Express adds higher-level
web-development features such as:

-   routing;
-   middleware;
-   request handling;
-   response helpers;
-   JSON responses.

This example builds on the previous Node.js example, which used Node's
built-in `http` module directly.

------------------------------------------------------------------------

## 1. Basic Architecture

A simplified Express request flow is:

``` text
Browser / API Client
        |
        | HTTP Request
        v
     Node.js
        |
        v
    Express.js
        |
        v
    Middleware
        |
        v
      Route
        |
        v
 Route Handler
        |
        v
HTTP / JSON Response
        |
        v
Browser / API Client
```

Express handles many common web-server tasks at a higher level than
Node's built-in `http` module.

------------------------------------------------------------------------

## 2. Project Structure

A simplified structure may look like:

``` text
08-express-basic/
├── server.js
├── package.json
├── package-lock.json
└── README.md
```

The exact server filename should match the scripts defined in the
project's `package.json`.

### Server file

The server file creates the Express application, defines routes and
middleware, and starts the HTTP server.

### `package.json`

Defines:

-   project metadata;
-   dependencies;
-   development dependencies;
-   npm scripts.

### `package-lock.json`

Records the installed dependency tree/version information managed by
npm.

------------------------------------------------------------------------

## 3. Prerequisites

This example requires Node.js and npm.

Check Node.js:

``` bash
node --version
```

Check npm:

``` bash
npm --version
```

Both commands should return version numbers.

------------------------------------------------------------------------

## 4. Install the Dependencies

From inside the `08-express-basic` directory:

``` bash
npm install
```

This reads `package.json` and installs the required packages.

Unlike the previous basic Node.js example, this project uses an external
package:

``` text
express
```

You can verify that Express is installed with:

``` bash
npm ls express
```

------------------------------------------------------------------------

## 5. Start the Express Development Server

Run:

``` bash
npm run dev
```

The application should be available at:

``` text
http://localhost:3000/
```

Keep the terminal running while testing the application.

Stop the server with:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 6. What `npm run dev` Does

`npm run dev` executes the script named `dev` in `package.json`.

For example, a project may use a script such as:

``` json
{
  "scripts": {
    "dev": "node server.js"
  }
}
```

or it may use a development utility that automatically restarts the
server when files change.

To see the actual scripts in this project, run:

``` bash
npm run
```

Conceptually:

``` text
npm run dev
     |
     v
package.json
     |
     v
"dev" script
     |
     v
Node.js
     |
     v
Express Application
```

------------------------------------------------------------------------

## 7. Test the Root Route

Open:

``` text
http://localhost:3000/
```

The request flow is:

``` text
Browser
   |
   | GET /
   v
Express
   |
   v
Matching Route
   |
   v
Route Handler
   |
   v
Response
   |
   v
Browser
```

You can also test it from another terminal:

``` bash
curl http://localhost:3000/
```

------------------------------------------------------------------------

## 8. Test the API Route

Open:

``` text
http://localhost:3000/api/info
```

or run:

``` bash
curl http://localhost:3000/api/info
```

This endpoint demonstrates an Express API response.

Conceptually:

``` text
Client
   |
   | GET /api/info
   v
Express Router
   |
   v
Route Handler
   |
   v
JavaScript Object
   |
   v
JSON Response
   |
   v
Client
```

------------------------------------------------------------------------

## 9. Express Routing

Express provides convenient route methods.

A basic GET route follows this pattern:

``` javascript
app.get("/", (req, res) => {
  res.send("Hello from Express");
});
```

The pieces are:

``` text
app.get(...)
```

Registers a route for an HTTP GET request.

``` text
"/"
```

Specifies the URL path.

``` text
req
```

Represents the incoming request.

``` text
res
```

Represents the outgoing response.

------------------------------------------------------------------------

## 10. JSON Responses

Express provides a convenient method for returning JSON:

``` javascript
res.json({
  framework: "Express",
  runtime: "Node.js"
});
```

Conceptually:

``` text
JavaScript Object
       |
       v
   res.json()
       |
       v
JSON HTTP Response
       |
       v
     Client
```

This is useful when Express is used to build REST APIs.

------------------------------------------------------------------------

## 11. Middleware

Middleware is one of the core concepts in Express.

Middleware is code that can run between the incoming request and the
final route handler.

Conceptually:

``` text
Request
   |
   v
Middleware 1
   |
   v
Middleware 2
   |
   v
Route Handler
   |
   v
Response
```

Middleware can be used for tasks such as:

-   parsing request data;
-   logging;
-   authentication;
-   authorization;
-   validation;
-   error handling.

A common example is:

``` javascript
app.use(express.json());
```

This middleware allows Express to parse JSON request bodies.

------------------------------------------------------------------------

## 12. Why Express Is Different from the Basic Node.js Example

The previous Node.js example uses the built-in `http` module directly.

Conceptually:

``` text
Node.js
   |
   v
http.createServer(...)
   |
   v
Manual request handling
```

Express adds abstractions:

``` text
Node.js
   |
   v
Express
   |
   +--> Routes
   +--> Middleware
   +--> Request helpers
   +--> Response helpers
   +--> JSON handling
```

Express does not replace Node.js.

Express **runs on Node.js**.

------------------------------------------------------------------------

## 13. Node.js vs. Express.js

  Concept                           Node.js Basic                    Express.js Basic
  --------------------------------- -------------------------------- ---------------------------------
  Primary role                      JavaScript runtime               Web framework
  Runs JavaScript outside browser   Yes                              Uses Node.js to do so
  HTTP capability                   Built-in `http` module           Higher-level Express API
  Routing                           Manual/basic                     `app.get()`, `app.post()`, etc.
  Middleware                        Must implement/manage directly   Core Express pattern
  JSON response helpers             Lower-level handling             `res.json()`
  Dependency on Express             No                               Yes

The main teaching point is:

``` text
Express depends on Node.js.
Node.js does not depend on Express.
```

------------------------------------------------------------------------

## 14. Express Compared with Flask

Express and Flask are useful to compare because both can be used to
build web applications and APIs.

  Concept              Flask                      Express
  -------------------- -------------------------- ---------------------------
  Language             Python                     JavaScript
  Runtime              Python                     Node.js
  Application object   `Flask(__name__)`          `express()`
  GET route            `@app.route(...)`          `app.get(...)`
  Request object       Flask `request`            Express `req`
  Response object      Flask return/`jsonify()`   Express `res`
  JSON parsing         Flask request handling     Commonly `express.json()`
  Middleware model     Supported                  Central Express concept

These are simplified comparisons for the examples in this repository.

------------------------------------------------------------------------

## 15. Recommended Run Sequence

From inside `08-express-basic`:

``` bash
node --version
npm --version

npm install
npm ls express

npm run dev
```

Then open:

``` text
http://localhost:3000/
```

and:

``` text
http://localhost:3000/api/info
```

------------------------------------------------------------------------

## 16. Using Two Terminals

### Terminal 1 --- Run Express

``` bash
npm run dev
```

Leave this terminal running.

### Terminal 2 --- Test the routes

``` bash
curl http://localhost:3000/
```

Then:

``` bash
curl http://localhost:3000/api/info
```

The workflow is:

``` text
Terminal 1                         Terminal 2
----------                         ----------
npm run dev
    |
    | Express server running
    |
    +---------------------------> curl GET /
    |
    +---------------------------> curl GET /api/info
```

------------------------------------------------------------------------

## 17. Troubleshooting: `node: command not found`

If:

``` bash
node --version
```

returns a command-not-found error, install Node.js before running the
example.

After installation, open a new terminal and verify:

``` bash
node --version
npm --version
```

------------------------------------------------------------------------

## 18. Troubleshooting: `npm: command not found`

npm normally comes with Node.js.

Verify:

``` bash
node --version
npm --version
```

Do not continue with `npm install` or `npm run dev` until npm is
available.

------------------------------------------------------------------------

## 19. Troubleshooting: `Cannot find module 'express'`

If Node reports:

``` text
Cannot find module 'express'
```

install the project dependencies:

``` bash
npm install
```

Then verify:

``` bash
npm ls express
```

Retry:

``` bash
npm run dev
```

------------------------------------------------------------------------

## 20. Troubleshooting: `Missing script: dev`

If:

``` bash
npm run dev
```

reports:

``` text
Missing script: "dev"
```

display the available scripts:

``` bash
npm run
```

Then inspect the `scripts` section in:

``` text
package.json
```

Use the script actually defined by the repository.

Do not add or rename a script unless you intend to modify the project
configuration.

------------------------------------------------------------------------

## 21. Troubleshooting: Port 3000 Is Already in Use

If the server reports that port `3000` is already in use, check whether
another Node or Express server is still running.

Stop the previous server with:

``` text
Ctrl+C
```

Then retry:

``` bash
npm run dev
```

If the project supports a configurable port, another port may be used
according to the server code.

------------------------------------------------------------------------

## 22. Troubleshooting: `/api/info` Returns 404

If:

``` text
http://localhost:3000/api/info
```

returns:

``` text
404 Not Found
```

check that:

1.  the Express server is running;
2.  the URL is exactly `/api/info`;
3.  the server code defines that route;
4.  you are using the correct port;
5.  the terminal does not show a startup or syntax error.

A route such as:

``` javascript
app.get("/api/info", ...)
```

must exist for a GET request to `/api/info`.

------------------------------------------------------------------------

## 23. Troubleshooting: Reinstall Dependencies

If the dependency installation becomes inconsistent:

``` bash
rm -rf node_modules
npm install
npm run dev
```

Do not delete project source files or `package.json`.

------------------------------------------------------------------------

## 24. Quick Command Reference

  Goal                       Command
  -------------------------- ---------------------------------------
  Check Node.js              `node --version`
  Check npm                  `npm --version`
  Install dependencies       `npm install`
  Check Express              `npm ls express`
  Show npm scripts           `npm run`
  Start development server   `npm run dev`
  Test root route            `curl http://localhost:3000/`
  Test API route             `curl http://localhost:3000/api/info`
  Open root route            `http://localhost:3000/`
  Open API route             `http://localhost:3000/api/info`
  Stop server                `Ctrl+C`

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain the relationship between Node.js and Express.js.
2.  Explain why Express is a framework while Node.js is a runtime.
3.  Create or identify an Express route.
4.  Explain the roles of `req` and `res`.
5.  Explain how Express returns JSON responses.
6.  Describe middleware at a basic level.
7.  Explain the purpose of `express.json()`.
8.  Explain what `npm run dev` does.
9.  Test Express endpoints using a browser and `curl`.
10. Compare the basic Node.js HTTP example with the Express example.
11. Compare the basic Express and Flask request/response models.
12. Trace an HTTP request through Express and back to the client.
