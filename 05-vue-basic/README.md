# 05 --- Vue Basic Example

This example demonstrates a basic **Vue application built with Vite**.

It introduces:

-   Vue Single-File Components (SFCs);
-   reactive state;
-   template rendering;
-   event handling;
-   Vue application mounting;
-   npm package management;
-   the Vite development server.

The example is intentionally small so students can focus on how Vue
connects JavaScript state, an HTML-like template, and user interactions.

------------------------------------------------------------------------

## 1. Basic Architecture

A simplified Vue application flow is:

``` text
Browser
   |
   v
index.html
   |
   v
src/main.js
   |
   | Creates and mounts Vue
   v
src/App.vue
   |
   +--> <template>
   +--> <script>
   +--> reactive state
   +--> event handlers
   |
   v
Rendered User Interface
   |
   v
Browser
```

When the user interacts with the page:

``` text
User Interaction
      |
      v
Vue Event Handler
      |
      v
Reactive State Changes
      |
      v
Vue Updates the DOM
      |
      v
Browser Displays Updated UI
```

Vue handles the UI update without requiring the developer to manually
rewrite the page's DOM for each state change.

------------------------------------------------------------------------

## 2. Typical Project Structure

A simplified Vite + Vue project looks like:

``` text
05-vue-basic/
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── src/
    ├── main.js
    └── App.vue
```

Depending on the exact project, additional files or directories may also
be present.

### `index.html`

Provides the HTML entry point used by Vite.

### `src/main.js`

Starts the Vue application and mounts the root component.

### `src/App.vue`

Contains the root Vue Single-File Component.

### `package.json`

Defines:

-   project metadata;
-   runtime dependencies;
-   development dependencies;
-   npm scripts.

### `vite.config.js`

Contains Vite configuration when the project needs explicit
configuration or plugins.

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

If either command returns:

``` text
command not found
```

Node.js is not installed or is not available on the system PATH.

------------------------------------------------------------------------

## 4. Install the Project Dependencies

From inside the `05-vue-basic` directory, run:

``` bash
npm install
```

This reads:

``` text
package.json
```

and installs the project's dependencies.

The installed packages are normally placed in:

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

Vite will print a local URL similar to:

``` text
http://localhost:5173/
```

Open the URL printed in the terminal.

The normal address is:

``` text
http://localhost:5173/
```

Keep the terminal running while using the application.

To stop the development server:

``` text
Ctrl+C
```

------------------------------------------------------------------------

## 6. What `npm run dev` Does

The command:

``` bash
npm run dev
```

runs the script named:

``` text
dev
```

from `package.json`.

A Vite project commonly contains a script similar to:

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
Vue Application in Browser
```

------------------------------------------------------------------------

## 7. Understanding `package.json`

`package.json` is a JSON file.

JSON does **not** support normal JavaScript comments, so comments such
as:

``` javascript
// this is a comment
```

should not be added to `package.json`.

This README provides the explanation instead.

Three important sections are:

### `dependencies`

Packages needed by the application at runtime.

For a Vue project, Vue itself is normally a dependency.

### `devDependencies`

Packages used during development, building, or tooling.

Vite and Vue-related Vite plugins are commonly development dependencies.

### `scripts`

Named commands that can be executed with npm.

For example:

``` json
{
  "scripts": {
    "dev": "vite"
  }
}
```

can be executed with:

``` bash
npm run dev
```

------------------------------------------------------------------------

## 8. Understanding a Vue Single-File Component

A Vue Single-File Component normally uses the extension:

``` text
.vue
```

For example:

``` text
App.vue
```

A component can combine:

``` text
<template>
<script>
<style>
```

in one file.

Conceptually:

``` text
App.vue
   |
   +--> Template: what the UI displays
   |
   +--> Script: state and application behavior
   |
   +--> Style: component appearance
```

Not every teaching example needs all three sections.

------------------------------------------------------------------------

## 9. Template

The `<template>` section describes what Vue renders.

For example:

``` vue
<template>
  <h1>{{ message }}</h1>
</template>
```

The expression:

``` text
{{ message }}
```

is Vue template interpolation.

Vue displays the current value of `message` in the page.

------------------------------------------------------------------------

## 10. Reactive State

Reactive state means the UI can automatically update when application
data changes.

Conceptually:

``` text
State
  |
  | changes
  v
Vue Reactivity System
  |
  v
Affected UI Updates
```

For example, a component may contain a reactive counter or message.

When the value changes, Vue updates the displayed value without
requiring a full browser-page reload.

------------------------------------------------------------------------

## 11. Event Handling

Vue can respond to browser events such as button clicks.

A template may use:

``` vue
<button @click="increment">
  Increment
</button>
```

The:

``` text
@click
```

syntax attaches a Vue click-event handler.

The flow becomes:

``` text
User clicks button
       |
       v
@click handler
       |
       v
JavaScript function executes
       |
       v
Reactive state changes
       |
       v
Vue updates the interface
```

------------------------------------------------------------------------

## 12. `main.js` and Application Mounting

The Vue application typically begins in:

``` text
src/main.js
```

A common pattern is:

``` javascript
import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
```

Conceptually:

``` text
App.vue
   |
   v
createApp(App)
   |
   v
mount("#app")
   |
   v
index.html
   |
   v
<div id="app"></div>
```

Vue mounts the root component into the matching HTML element.

------------------------------------------------------------------------

## 13. Vue Compared with the Previous Examples

  --------------------------------------------------------------------------
  Concept        Flask          FastAPI        Streamlit      Vue
  -------------- -------------- -------------- -------------- --------------
  Primary role   Web app + API  REST API       Python UI      Frontend UI
  in these                                                    
  examples                                                    

  Primary        Python         Python         Python         JavaScript
  language                                                    

  Runs in        HTML output    API            Streamlit UI   Vue
  browser                       client/docs                   application

  Reactive UI    Requires       Requires       Built in       Core feature
                 frontend logic frontend                      

  Components     Not primary    Not primary    Python UI      Vue components
                 concept        concept        elements       

  Package        pip            pip            pip            npm
  manager                                                     

  Development    Flask          Uvicorn        Streamlit      Vite
  server                                                      
  --------------------------------------------------------------------------

These are simplified distinctions for the teaching examples in this
repository.

------------------------------------------------------------------------

## 14. Recommended Run Sequence

From inside `05-vue-basic`:

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

## 15. Troubleshooting: `node: command not found`

If:

``` bash
node --version
```

returns:

``` text
command not found: node
```

Node.js must be installed before running this example.

After installation, open a new terminal and verify:

``` bash
node --version
npm --version
```

Both commands should return version numbers.

------------------------------------------------------------------------

## 16. Troubleshooting: `npm: command not found`

Because npm is normally installed with Node.js, this usually indicates
that Node.js is not installed correctly or its executable directory is
not on the system PATH.

Verify:

``` bash
node --version
npm --version
```

Do not continue with:

``` bash
npm install
```

until npm is available.

------------------------------------------------------------------------

## 17. Troubleshooting: Missing Packages

If Vite reports that a package cannot be found, first make sure the
dependencies were installed:

``` bash
npm install
```

Then retry:

``` bash
npm run dev
```

If `node_modules/` was removed, running `npm install` recreates the
installed dependency directory from `package.json` and the lock file.

------------------------------------------------------------------------

## 18. Troubleshooting: Vue Vite Plugin Error

If Vite reports an error involving:

``` text
@vitejs/plugin-vue
```

check whether the package is installed:

``` bash
npm ls @vitejs/plugin-vue
```

If the project's `vite.config.js` imports the Vue plugin but the package
is missing, install it as a development dependency:

``` bash
npm install --save-dev @vitejs/plugin-vue
```

Then restart:

``` bash
npm run dev
```

The configuration commonly uses the plugin so Vite can process `.vue`
Single-File Components.

------------------------------------------------------------------------

## 19. Troubleshooting: Changes Do Not Appear

Vite normally supports fast development updates.

If a code change does not appear:

1.  Confirm `npm run dev` is still running.
2.  Check the terminal for syntax or import errors.
3.  Save the source file.
4.  Refresh the browser if necessary.
5.  Verify that you edited the file actually imported by the
    application.

For example, changing an unused file will not affect the rendered
application.

------------------------------------------------------------------------

## 20. Troubleshooting: Port 5173 Is Already in Use

If port `5173` is unavailable, Vite may automatically select another
port.

Always use the URL printed by Vite in the terminal.

For example:

``` text
Local: http://localhost:5174/
```

In that case, open:

``` text
http://localhost:5174/
```

instead of assuming the application is on port `5173`.

------------------------------------------------------------------------

## 21. Troubleshooting: Reinstall Dependencies

If the dependency installation becomes inconsistent, you can reinstall
the project dependencies.

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

## 22. Quick Command Reference

  ---------------------------------------------------------------------------------
  Goal                                Command
  ----------------------------------- ---------------------------------------------
  Check Node.js                       `node --version`

  Check npm                           `npm --version`

  Install dependencies                `npm install`

  Start Vite                          `npm run dev`

  Check Vue plugin                    `npm ls @vitejs/plugin-vue`

  Install Vue Vite plugin if required `npm install --save-dev @vitejs/plugin-vue`

  Stop Vite                           `Ctrl+C`

  Normal local URL                    `http://localhost:5173/`
  ---------------------------------------------------------------------------------

------------------------------------------------------------------------

## Learning Outcomes

After completing this example, students should be able to:

1.  Explain the role of Vue as a frontend framework.
2.  Explain the role of Vite in the development workflow.
3.  Identify the purpose of `package.json`.
4.  Distinguish `dependencies`, `devDependencies`, and `scripts`.
5.  Explain what a Vue Single-File Component is.
6.  Identify the purpose of `<template>`, `<script>`, and `<style>`.
7.  Explain reactive state at a basic level.
8.  Explain how Vue event handling connects user interaction to
    application logic.
9.  Describe how `main.js` mounts the Vue application.
10. Install dependencies and run a Vue application with npm.
11. Trace a user interaction from a Vue component through reactive state
    and back to the rendered browser interface.
