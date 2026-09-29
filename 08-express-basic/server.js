// Express is a web framework/library that runs on the Node.js runtime.
import express from 'express'
const app = express()
const port = 3000

// Middleware runs during the request/response pipeline. express.json() parses
// JSON request bodies and places the parsed value on request.body.
app.use(express.json())

// A route combines an HTTP method, URL path, and handler function.
app.get('/', (request, response) => {
  response.send('<h1>Hello from Express!</h1><p>Express is running on Node.js.</p>')
})

app.get('/api/info', (request, response) => {
  // response.json() serializes this JavaScript object as JSON.
  response.json({ runtime: 'Node.js', framework: 'Express.js', purpose: 'Web/API server' })
})

app.post('/api/echo', (request, response) => {
  // Echo the validated/parsing demonstration body back to the caller.
  response.status(201).json({ received: request.body })
})

app.listen(port, () => {
  console.log(`Express server running at http://localhost:${port}/`)
})
