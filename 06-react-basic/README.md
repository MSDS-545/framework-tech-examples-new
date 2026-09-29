# 06 --- React Basic Example

This example demonstrates a basic **React application built with Vite**.

It introduces:

-   React function components;
-   JSX;
-   component rendering;
-   state;
-   event handling;
-   npm package management;
-   the Vite development server.

The example is intentionally small so students can focus on how React
connects components, application state, user events, and the rendered
browser interface.

------------------------------------------------------------------------

## 1. Basic Architecture

A simplified React application flow is:

``` text
Browser
   |
   v
index.html
   |
   v
src/main.jsx
   |
   | Creates the React root
   v
src/App.jsx
   |
   +--> Function Component
   +--> JSX
   +--> State
   +--> Event Handlers
   |
   v
Rendered User Interface
   |
   v
Browser
```

When a user interacts with the application:

``` text
User Interaction
      |
      v
Event Handler
      |
      v
State Changes
      |
      v
React Re-renders Component
      |
      v
Browser Displays Updated UI
```

React updates the affected interface based on the component's current
state.

------------------------------------------------------------------------

## 2. Typical Project Structure

A simplified Vite + React project looks like:

``` text
06-react-basic/
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── src/
    ├── main.jsx
    └── App.jsx
```

Depending on the exact project, additional files or directories may also
be present.

### `index.html`

Provides the HTML entry point used by Vite.

### `src/main.jsx`

Creates the React root and renders the main application component.

### `src/App.jsx`

Contains the primary React function component for this example.

### `package.json`

Defines project metadata, dependencies, development dependencies, and
npm scripts.

### `vite.config.js`

Contains Vite configuration when explicit configuration or plugins are
needed.

------------------------------------------------------------------------

## 3. Prerequisites

This example requires **Node.js** and **npm**.

Check Node.js:

``` bash
node --version
```

Check npm:

``` bash
npm --version
```

Both commands should return version numbers.

If either command returns `command not found`, Node.js is not installed
correctly or is not available on the system PATH.

------------------------------------------------------------------------

## 4. Install the Dependencies

From inside the `06-react-basic` directory, run:

``` bash
npm install
```

This reads:

``` text
package.json
```

and installs the project dependencies.

Installed packages are normally placed in:

``` text
node_modules/
```

The `node_modules/` directory should normally not be committed to Git.

------------------------------------------------------------------------

## 5. Start the Vite Development Server

Run:

``` bash
npm run dev
```

Vite prints a local URL similar to:

``` text
http://localhost:5173/
```

Open the URL printed in the terminal.

Keep the terminal running while using the application.

Stop the development server with:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 6. What `npm run dev` Does

The command:

``` bash
npm run dev
```

runs the script named `dev` from `package.json`.

A Vite project commonly contains:

``` json
{
  "scripts": {
    "dev": "vite"
  }
}
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
Vite
     |
     v
Development Server
     |
     v
React Application
```

------------------------------------------------------------------------

## 7. Understanding `package.json`

`package.json` is a JSON file.

JSON does **not** support normal JavaScript comments. Do not add
comments such as:

``` javascript
// React dependency
```

inside `package.json`.

Use documentation such as this README to explain the file.

Important sections include:

### `dependencies`

Packages required by the application.

React projects commonly include packages such as React and React DOM.

### `devDependencies`

Packages used for development, building, or tooling.

Vite and React-related Vite plugins are commonly development
dependencies.

### `scripts`

Named npm commands.

For example:

``` json
{
  "scripts": {
    "dev": "vite"
  }
}
```

is executed with:

``` bash
npm run dev
```

------------------------------------------------------------------------

## 8. React Function Components

A React function component is a JavaScript function that returns JSX.

A simplified example is:

``` jsx
function Welcome() {
  return <h1>Hello</h1>;
}
```

Conceptually:

``` text
Function Component
       |
       v
      JSX
       |
       v
React Rendering
       |
       v
Browser UI
```

Components allow the user interface to be divided into reusable pieces.

------------------------------------------------------------------------

## 9. Understanding JSX

JSX allows developers to describe interface structure using syntax that
resembles HTML inside JavaScript.

For example:

``` jsx
const title = "React Example";

return <h1>{title}</h1>;
```

The braces:

``` text
{title}
```

allow a JavaScript expression to be inserted into JSX.

JSX is not simply an HTML file. It is part of the React/JavaScript
source and is processed by the development/build toolchain.

------------------------------------------------------------------------

## 10. State

State stores data that can change while a component is being used.

A common React pattern uses:

``` jsx
useState()
```

For example:

``` jsx
const [count, setCount] = useState(0);
```

Conceptually:

``` text
Current State
     |
     | setState-style update
     v
New State
     |
     v
React Re-renders
     |
     v
Updated UI
```

The state value influences what the component displays.

------------------------------------------------------------------------

## 11. Event Handling

React can respond to browser events such as button clicks.

For example:

``` jsx
<button onClick={handleClick}>
  Click Me
</button>
```

The flow is:

``` text
User clicks button
       |
       v
onClick
       |
       v
handleClick()
       |
       v
State may change
       |
       v
Component re-renders
       |
       v
Updated browser UI
```

React event handlers are JavaScript functions.

------------------------------------------------------------------------

## 12. `main.jsx` and Application Rendering

The React application commonly starts in:

``` text
src/main.jsx
```

A typical Vite/React entry point uses React DOM to render the root
component into the page.

Conceptually:

``` text
App.jsx
   |
   v
React
   |
   v
ReactDOM
   |
   v
<div id="root"></div>
   |
   v
Browser
```

The matching root element is normally defined in:

``` text
index.html
```

------------------------------------------------------------------------

## 13. React Compared with Vue

Both the Vue and React examples in this repository demonstrate
component-based frontend development, but they use different syntax and
APIs.

  -----------------------------------------------------------------------
  Concept                 Vue Basic               React Basic
  ----------------------- ----------------------- -----------------------
  Frontend                Vue                     React
  framework/library                               

  Main component          `App.vue`               `App.jsx`

  UI syntax               Vue template            JSX

  Component format        Single-File Component   JavaScript/JSX function
                                                  component

  State                   Vue reactivity APIs     React state APIs such
                                                  as `useState`

  Click event             `@click`                `onClick`

  Entry point             `main.js`               `main.jsx`

  Development server      Vite                    Vite

  Package manager         npm                     npm
  -----------------------------------------------------------------------

The goal is not to identify one as universally better. The examples show
two common approaches to building reactive frontend applications.

------------------------------------------------------------------------

## 14. React Compared with the Python Framework Examples

  Example     Primary teaching role
  ----------- ------------------------------
  Django      Full web-framework structure
  Flask       Webpage + API
  FastAPI     Typed REST API
  Streamlit   Python-first interactive UI
  Vue         Component-based frontend
  React       Component-based frontend

React normally runs in the browser and can communicate with a backend
API such as Flask or FastAPI in a larger full-stack application.

------------------------------------------------------------------------

## 15. Recommended Run Sequence

From inside `06-react-basic`:

``` bash
node --version
npm --version

npm install
npm run dev
```

Then open the URL printed by Vite, normally:

``` text
http://localhost:5173/
```

------------------------------------------------------------------------

## 16. Troubleshooting: `node: command not found`

If:

``` bash
node --version
```

returns a command-not-found error, Node.js must be installed before
running the example.

After installation, open a new terminal and verify:

``` bash
node --version
npm --version
```

------------------------------------------------------------------------

## 17. Troubleshooting: `npm: command not found`

npm is normally installed with Node.js.

If npm cannot be found, verify:

``` bash
node --version
npm --version
```

Do not continue with `npm install` until npm is available.

------------------------------------------------------------------------

## 18. Troubleshooting: Missing Packages

If Vite reports that a package cannot be found, install the project
dependencies:

``` bash
npm install
```

Then retry:

``` bash
npm run dev
```

If `node_modules/` was removed, `npm install` recreates the installed
dependencies from the project configuration.

------------------------------------------------------------------------

## 19. Troubleshooting: React Vite Plugin Error

If Vite reports an error involving:

``` text
@vitejs/plugin-react
```

check whether it is installed:

``` bash
npm ls @vitejs/plugin-react
```

If `vite.config.js` imports the React plugin but the package is missing,
install it as a development dependency:

``` bash
npm install --save-dev @vitejs/plugin-react
```

Then restart:

``` bash
npm run dev
```

------------------------------------------------------------------------

## 20. Troubleshooting: Changes Do Not Appear

If a source-code change does not appear:

1.  Confirm `npm run dev` is still running.
2.  Check the terminal for syntax or import errors.
3.  Save the edited file.
4.  Verify that the edited component is actually imported.
5.  Refresh the browser if necessary.

Vite normally provides fast development updates while the server is
running.

------------------------------------------------------------------------

## 21. Troubleshooting: Port 5173 Is Already in Use

If port `5173` is unavailable, Vite may automatically select another
port.

For example:

``` text
Local: http://localhost:5174/
```

Always use the URL printed by Vite rather than assuming the application
is running on port `5173`.

------------------------------------------------------------------------

## 22. Troubleshooting: Reinstall Dependencies

If the dependency installation becomes inconsistent, reinstall it.

On macOS/Linux:

``` bash
rm -rf node_modules
npm install
npm run dev
```

Do not delete project source files such as:

``` text
src/
package.json
vite.config.js
```

when reinstalling dependencies.

------------------------------------------------------------------------

## 23. Quick Command Reference

  -----------------------------------------------------------------------------------
  Goal                                Command
  ----------------------------------- -----------------------------------------------
  Check Node.js                       `node --version`

  Check npm                           `npm --version`

  Install dependencies                `npm install`

  Start Vite                          `npm run dev`

  Check React Vite plugin             `npm ls @vitejs/plugin-react`

  Install React Vite plugin if        `npm install --save-dev @vitejs/plugin-react`
  required                            

  Stop Vite                           `Ctrl+C`

  Normal local URL                    `http://localhost:5173/`
  -----------------------------------------------------------------------------------

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain the role of React in frontend development.
2.  Explain the role of Vite in the development workflow.
3.  Identify the purpose of `package.json`.
4.  Distinguish `dependencies`, `devDependencies`, and `scripts`.
5.  Explain what a React function component is.
6.  Explain the purpose of JSX.
7.  Explain React state at a basic level.
8.  Explain how an event handler responds to user interaction.
9.  Describe how a state change causes a component to re-render.
10. Explain the role of `main.jsx` and the root component.
11. Install dependencies and run a React application with npm.
12. Compare the basic React and Vue component models used in this
    repository.
