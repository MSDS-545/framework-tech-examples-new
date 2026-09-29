// Node.js can run JavaScript outside the browser. This built-in module provides
// low-level HTTP server functionality without a third-party web framework.
import http from 'node:http'

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((request, response) => {
  // statusCode and headers describe the HTTP response sent to the browser.
  response.statusCode = 200
  response.setHeader('Content-Type', 'text/html; charset=utf-8')
  // end() sends the response body and completes the request.
  response.end('<h1>Hello from Node.js!</h1><p>This uses the built-in HTTP module.</p>')
})

server.listen(port, hostname, () => {
  console.log(`Node server running at http://${hostname}:${port}/`)
})
