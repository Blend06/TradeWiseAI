import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosClient from '../../utils/api';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const ControlPanel = () => {
  const [data, setData] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem('accessToken');

      if (!token) {
        alert('No access token found.');
        navigate('/');
        return;
      }

      try {
        // Check staff status
        const userResponse = await axiosClient.get('/users/me/')

        if (!userResponse.data.is_staff) {
          alert('Unauthorized access.');
          navigate('/');
          return;
        }

        // Fetch admin data
        const dashboardResponse = await axiosClient.get('/control-panel-data/');

        setData(dashboardResponse.data);
      } catch (error) {
        console.log('Error fetching data: ', error);
        navigate('/')
      }
    };

    fetchData();
  }, [navigate]);

  const chartData = {
    labels: [
      'Users',
      'News',
    ],
    datasets: [
      {
        label: 'Counts',
        data: [
          data.total_users || 0,
          data.total_news || 0,
        ],
        backgroundColor: [
          '#007bff',
          '#6610f2',
        ],
        borderColor: '#ffffff',
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: 'Dashboard Overview - Summary Chart',
      },
    },
  };

  return (
    <div className="container py-5">
      <h1 className="text-center mb-5 fw-bold text-primary">Admin Control Panel</h1>

      <div className="d-flex justify-content-center flex-wrap gap-2 mb-5">
        <button className="btn btn-outline-primary" onClick={() => navigate('/news')}>
          Manage News
        </button>
        <button className="btn btn-outline-primary" onClick={() => navigate('/users')}>
          Manage Users
        </button>
       
      </div>

      <div className="card shadow mb-5">
        <div className="card-body">
          <h2 className="mb-4 fw-bold text-danger">Dashboard Overview</h2>

          <div className="chart-container mb-4">
            <Bar data={chartData} options={chartOptions} />
          </div>

          <h3 className="mt-4">Summary</h3>
          <ul className="list-group">
            <li className="list-group-item">Total Users: {data.total_users || 0}</li>
            <li className="list-group-item">Total News: {data.total_news || 0}</li>
          </ul>

          <div className="text-center mt-4">
            <button className="btn btn-link" onClick={() => navigate('/')}>
              Return to Homepage
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ControlPanel;
