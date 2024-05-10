import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Homepage from './pages/Homepage';
import NotFound from './pages/NotFound'
import AgentTable from './components/tables/AgentTable'
import ReferralTable from './components/tables/ReferralTable'
import ClientTable from './components/tables/ClientTable'
import DeliveryTable from './components/tables/DeliveryTable'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Homepage />,
    errorElement: <NotFound />,
    children: [
      {
        path: '/agents',
        element: <AgentTable />
      },
      {
        path: '/referrals',
        element: <ReferralTable />
      },
      {
        path: '/clients',
        element: <ClientTable />
      },
      {
        path: '/deliveries',
        element: <DeliveryTable />
      },
    ]
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
