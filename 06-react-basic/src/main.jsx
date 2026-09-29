// StrictMode enables additional development checks; createRoot starts React 18+ rendering.
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

// Render the root App component inside <div id="root"> from index.html.
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
