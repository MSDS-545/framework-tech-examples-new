# 07 --- Node.js Basic Example

This example demonstrates a basic web server using **Node.js**.

The most important distinction in this example is:

> **Node.js is a JavaScript runtime, not a frontend framework.**

Unlike the previous Vue and React examples, Node.js is not being used to
build a browser user interface. Instead, JavaScript runs outside the
browser and creates a server.

This example deliberately uses Node's built-in:

``` text
http
```

module and does **not** use Express.

The example introduces:

-   Node.js as a JavaScript runtime;
-   server-side JavaScript;
-   Node's built-in `http` module;
-   HTTP requests and responses;
-   npm scripts;
-   `package.json`;
-   starting and stopping a Node.js server.

------------------------------------------------------------------------

## 1. Basic Architecture

The request flow is:

``` text
Browser
   |
   | HTTP GET /
   v
Node.js Server
   |
   v
Built-in http Module
   |
   v
Request Handler
   |
   v
HTTP Response
   |
   v
Browser
```

Unlike a frontend React or Vue application, the JavaScript in this
example executes on the server.

------------------------------------------------------------------------

## 2. Node.js Runtime Model

In a browser-based JavaScript application:

``` text
Browser
   |
   v
JavaScript
   |
   v
User Interface
```

In this Node.js example:

``` text
Operating System
      |
      v
   Node.js
      |
      v
JavaScript Server Code
      |
      v
HTTP Server
      |
      v
Browser / Client
```

Node.js provides the runtime environment that allows JavaScript to
execute outside the browser.

------------------------------------------------------------------------

## 3. Project Structure

A simplified project structure is:

``` text
07-node-basic/
├── server.js
├── package.json
├── package-lock.json
└── README.md
```

The exact server filename should match the script defined in the
project's `package.json`.

### `server.js`

Contains the JavaScript code that creates the HTTP server.

### `package.json`

Contains project metadata and npm scripts.

### `package-lock.json`

Records the dependency tree/version information managed by npm.

Because this example uses Node's built-in `http` module, it does not
need Express.

------------------------------------------------------------------------

## 4. Prerequisites

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

If either command returns a command-not-found error, Node.js is not
installed correctly or is not available on the system PATH.

------------------------------------------------------------------------

## 5. Install Project Dependencies

If the project contains a `package.json`, it is good practice to run:

``` bash
npm install
```

For this basic example, there may be few or no external runtime
dependencies because the HTTP server uses Node's built-in `http` module.

Running `npm install` still allows npm to process the project's package
configuration and lock file.

------------------------------------------------------------------------

## 6. Start the Node.js Server

Run:

``` bash
npm start
```

The server should start on:

``` text
http://localhost:3000/
```

Keep the terminal running while using the application.

Open:

``` text
http://localhost:3000/
```

in a browser.

To stop the server:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 7. What `npm start` Does

`npm start` runs the `start` script defined in:

``` text
package.json
```

For example, a project may contain:

``` json
{
  "scripts": {
    "start": "node server.js"
  }
}
```

The flow is:

``` text
npm start
    |
    v
package.json
    |
    v
"start" script
    |
    v
node server.js
    |
    v
Node.js HTTP Server
```

This lets the repository provide a consistent command for starting the
application.

------------------------------------------------------------------------

## 8. Understanding `package.json`

`package.json` is a JSON file that describes a Node.js project.

Important sections can include:

### `scripts`

Defines commands such as:

``` json
{
  "scripts": {
    "start": "node server.js"
  }
}
```

### `dependencies`

Lists external packages required by the application.

This basic example uses Node's built-in HTTP module, so an Express
dependency is not required.

### `devDependencies`

Lists packages used primarily during development or testing.

Because `package.json` is JSON, it cannot contain normal JavaScript
comments.

Do not add:

``` javascript
// comment
```

inside `package.json`.

------------------------------------------------------------------------

## 9. The Built-In `http` Module

Node.js includes an HTTP module.

A simplified example is:

``` javascript
const http = require("http");
```

or, depending on the project's module configuration:

``` javascript
import http from "http";
```

The module can create an HTTP server without installing a separate web
framework.

Conceptually:

``` text
Node.js
   |
   v
http module
   |
   v
createServer(...)
   |
   v
Request Handler
   |
   v
listen(...)
```

------------------------------------------------------------------------

## 10. Request and Response Objects

A Node HTTP server receives information about the incoming request and
creates a response.

Conceptually:

``` text
Client
   |
   | Request
   v
Node.js
   |
   +--> Request Object
   |
   +--> Application Logic
   |
   +--> Response Object
   |
   v
Client
```

The request can contain information such as:

-   the URL;
-   HTTP method;
-   headers.

The response can contain:

-   an HTTP status code;
-   response headers;
-   response body.

------------------------------------------------------------------------

## 11. Listening on a Port

The server must listen on a network port.

This example uses:

``` text
3000
```

so the application is available at:

``` text
http://localhost:3000/
```

Conceptually:

``` text
Node.js Process
      |
      v
Listen on Port 3000
      |
      v
http://localhost:3000/
      |
      v
Browser Request
```

------------------------------------------------------------------------

## 12. Why This Example Does Not Use Express

Express is a popular Node.js web framework, but this example
intentionally starts with Node's built-in HTTP capabilities.

This lets students distinguish:

``` text
Node.js
```

from:

``` text
Express.js
```

Node.js provides the runtime.

Express provides higher-level web-framework features that run on
Node.js.

Conceptually:

``` text
Node.js
   |
   +--> Built-in http module
   |
   +--> Express can run on top of Node.js
```

The later Express example can then show what the framework adds.

------------------------------------------------------------------------

## 13. Node.js Compared with React and Vue

A common source of confusion is treating Node.js as another frontend
framework.

For these examples:

  Technology   Primary role
  ------------ --------------------------------------------
  Vue          Frontend framework
  React        Frontend UI library
  Node.js      JavaScript runtime
  Express      Backend web framework that runs on Node.js

React and Vue code primarily creates browser interfaces.

Node.js allows JavaScript to run outside the browser and can be used to
create servers, command-line programs, development tools, and backend
applications.

------------------------------------------------------------------------

## 14. Node.js Compared with Python

A useful conceptual comparison is:

``` text
Python source code
      |
      v
Python interpreter
      |
      v
Program executes
```

and:

``` text
JavaScript source code
      |
      v
Node.js runtime
      |
      v
Program executes
```

This is a simplified comparison intended to help students understand the
role of Node.js as a runtime.

------------------------------------------------------------------------

## 15. Recommended Run Sequence

From inside `07-node-basic`:

``` bash
node --version
npm --version

npm install
npm start
```

Then open:

``` text
http://localhost:3000/
```

Keep the terminal running while using the server.

Stop it with:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 16. Test with `curl`

While the Node.js server is running in **Terminal 1**, open **Terminal
2** and run:

``` bash
curl http://localhost:3000/
```

This sends an HTTP GET request without using the browser.

The workflow is:

``` text
Terminal 1                         Terminal 2
----------                         ----------
npm start
    |
    | Node server running
    |
    +---------------------------> curl http://localhost:3000/
    |
    | <------------------------- HTTP response
```

This helps demonstrate that the server responds to HTTP clients, not
only browsers.

------------------------------------------------------------------------

## 17. Troubleshooting: `node: command not found`

If:

``` bash
node --version
```

returns a command-not-found error, Node.js must be installed before
running the project.

After installation, open a new terminal and verify:

``` bash
node --version
npm --version
```

------------------------------------------------------------------------

## 18. Troubleshooting: `npm: command not found`

npm is normally installed with Node.js.

Verify:

``` bash
node --version
npm --version
```

Do not continue with `npm start` until npm is available.

------------------------------------------------------------------------

## 19. Troubleshooting: `Missing script: start`

If:

``` bash
npm start
```

reports:

``` text
Missing script: "start"
```

inspect the scripts in:

``` text
package.json
```

You can also run:

``` bash
npm run
```

to display available npm scripts.

The project needs a `start` script that points to its actual server
file.

For example:

``` json
{
  "scripts": {
    "start": "node server.js"
  }
}
```

Do not change the filename to `server.js` unless that is the actual
server file in the repository.

------------------------------------------------------------------------

## 20. Troubleshooting: Server File Cannot Be Found

If Node reports that it cannot find the server file, check the current
directory:

``` bash
pwd
ls
```

Make sure you are inside the `07-node-basic` directory.

Then inspect:

``` text
package.json
```

to see which file the `start` script runs.

------------------------------------------------------------------------

## 21. Troubleshooting: Port 3000 Is Already in Use

If the application reports that port `3000` is already in use, another
process may already be listening on that port.

First check whether another copy of the example is still running in
another terminal.

Stop the old server with:

``` text
Ctrl+C
```

and retry:

``` bash
npm start
```

If the application supports a configurable port, another port can be
used, but the exact method depends on how the server code reads its port
configuration.

------------------------------------------------------------------------

## 22. Troubleshooting: Browser Cannot Connect

If the browser cannot connect to:

``` text
http://localhost:3000/
```

check that:

1.  `npm start` is still running.
2.  The terminal does not show an application error.
3.  The server is listening on port `3000`.
4.  You are using the URL printed or configured by the application.

The server process must remain running while the browser sends requests.

------------------------------------------------------------------------

## 23. Quick Command Reference

  Goal                           Command
  ------------------------------ -------------------------------
  Check Node.js                  `node --version`
  Check npm                      `npm --version`
  Install project dependencies   `npm install`
  Show npm scripts               `npm run`
  Start server                   `npm start`
  Test with curl                 `curl http://localhost:3000/`
  Open in browser                `http://localhost:3000/`
  Stop server                    `Ctrl+C`

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain that Node.js is a JavaScript runtime rather than a frontend
    framework.
2.  Explain how JavaScript can execute outside a web browser.
3.  Describe the role of Node's built-in `http` module.
4.  Explain the basic HTTP request/response flow.
5.  Explain why a server listens on a port.
6.  Explain the role of `package.json`.
7.  Explain what `npm start` does.
8.  Distinguish Node.js from Express.
9.  Distinguish Node.js from frontend technologies such as React and
    Vue.
10. Start and stop a basic Node.js HTTP server.
11. Test a Node.js HTTP server with both a browser and `curl`.
