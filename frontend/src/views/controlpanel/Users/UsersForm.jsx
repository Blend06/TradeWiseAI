import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axiosClient from '../../../utils/api';

const UsersForm = () => {
  const { userId } = useParams();
  const navigate = useNavigate();

  const [userData, setUserData] = useState({
    username: '',
    email: '',
    password: '',
    is_staff: false,
  });
  const [currentUser, setCurrentUser] = useState({
    is_staff: false,
    is_superuser: false,
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [passwordTouched, setPasswordTouched] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      alert('No access token found.');
      navigate('/');
      return;
    }
    axiosClient.get('/users/me/').then(res => setCurrentUser(res.data)).catch(console.error);
  }, [navigate]);

  useEffect(() => {
    if (!userId) return;
    setLoading(true);
    axiosClient.get(`/users/${userId}/`)
      .then(({ data: user }) => {
        setUserData({
          username: user.username,
          email: user.email,
          password: '',
          is_staff: user.is_staff,
        });
        setPasswordTouched(false);
      })
      .catch(() => setError('Failed to load user details'))
      .finally(() => setLoading(false));
  }, [userId, navigate]);

  const handleChange = e => {
    const { name, value, type, checked } = e.target;
    if (name === 'password') setPasswordTouched(true);
    setUserData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const pwd = userData.password;
    const pwdRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!userId || passwordTouched) {
      if (!pwd || !pwdRegex.test(pwd)) {
        alert('Password must be at least 8 characters long and include letters and numbers.');
        return;
      }
    }
    setLoading(true);
    try {
      if (userId) {
        const payload = { ...userData };
        if (!passwordTouched) delete payload.password;
        await axiosClient.patch(`/users/${userId}/`, payload);
        alert('User updated successfully!');
      } else {
        await axiosClient.post('/users/', userData);
        alert('User created successfully!');
      }
      navigate('/users');
    } catch {
      setError('Failed to save user');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading…</div>;
  if (error)   return <div>{error}</div>;

  const disableUsername = userId && !currentUser.is_staff && !currentUser.is_superuser;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-danger">
        {userId ? 'Edit User' : 'Create User'}
      </h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="username">Username</label>
          <input
            id="username"
            name="username"
            type="text"
            className="form-control"
            value={userData.username}
            onChange={handleChange}
            required
            disabled={disableUsername}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            className="form-control"
            value={userData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password">
            {userId ? 'New Password (optional)' : 'Password (required)'}
          </label>
          <input
            id="password"
            name="password"
            type="password"
            className="form-control"
            value={userData.password}
            onChange={handleChange}
          />
        </div>
        <div className="form-check mb-3">
          <input
            id="is_staff"
            name="is_staff"
            type="checkbox"
            className="form-check-input"
            checked={userData.is_staff}
            onChange={handleChange}
          />
          <label className="form-check-label" htmlFor="is_staff">
            Is Staff?
          </label>
        </div>
        <button type="submit" className="btn btn-primary">
          {userId ? 'Update User' : 'Create User'}
        </button>
      </form>
    </div>
  );
};

export default UsersForm;
