import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from './routes/root';
import Profile from './routes/profile';
import Report from './routes/report';
import API from './routes/api';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      { path: "/profile", element: <Profile/> },
      { path: "/report", element: <Report/> },
      { path: "/mtgrest", element: <API/>}
    ]
  }
]);



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
