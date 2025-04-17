import React from 'react';
import ReactDOM from 'react-dom/client'; // Make sure to import from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'; // Import BrowserRouter

import App from './App'; // Import App component
import './assets/scss/style.scss';

const root = ReactDOM.createRoot(document.getElementById('root')); // Create root element

root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);