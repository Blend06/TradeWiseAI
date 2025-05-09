import axios from 'axios';

const axiosClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: true, 
});

axiosClient.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default axiosClient;
