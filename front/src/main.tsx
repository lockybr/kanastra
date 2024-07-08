import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { App } from './app'
import { FileProvider } from '@/components/ui/file'
import './global.css'
import { Toaster } from '@/components/ui/toaster'


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
      <FileProvider>
        <App />
        <Toaster />
      </FileProvider>
    </BrowserRouter>
  </React.StrictMode>,
)
