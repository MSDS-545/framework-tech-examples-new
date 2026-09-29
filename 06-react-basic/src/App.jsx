// useState lets a function component remember state between renders.
import { useState } from 'react'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    // JSX resembles HTML but is JavaScript syntax used to describe UI.
    <main style={{ fontFamily: 'sans-serif', maxWidth: 700, margin: '3rem auto' }}>
      <h1>Hello from React!</h1>
      <p>The button has been clicked {count} time(s).</p>
      {/* React event handlers receive JavaScript functions. */}
      <button onClick={() => setCount(count + 1)}>Click Me</button>
    </main>
  )
}
