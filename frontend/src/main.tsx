import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.tsx'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import "./styles.css"
import Root from './routes/root';
import Portfolio from './routes/portfolio';
import DSML from './routes/dsml';
import API from './routes/api';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      { path: "/portfolio", element: <Portfolio/> },
      { path: "/dsml", element: <DSML/> },
      { path: "/mtgrest", element: <API/>}
    ]
  }
]);



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
