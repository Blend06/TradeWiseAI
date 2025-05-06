import React, { useEffect, useState } from 'react';
import axiosClient from '../../../utils/api';
import { useNavigate } from 'react-router-dom';

const UsersPage = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    axiosClient.get('/users/')
      .then(({ data }) => setUsers(data))
      .catch(() => setError('Failed to load users data'))
      .finally(() => setLoading(false));
  }, [navigate]);

  const handleDelete = async userId => {
    
    if (!window.confirm('⚠️ Are you sure you want to delete this user?')) 
      return;
    
    try {
      await axiosClient.delete(`/users/${userId}/`);
      setUsers(users.filter(u => u.Userid !== userId));
    } catch {
      alert('Failed to delete user');
    }
  };

  if (loading) return <div>Loading users…</div>;
  if (error)   return <div>{error}</div>;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-danger">Manage Users</h1>

      <button className="btn btn-primary mb-3" onClick={() => navigate('/users/new')}>
        Create New User
      </button>

      {users.length > 0 ? (
        <div className="table-responsive">
          <table className="table table-bordered table-striped">
            <thead>
              <tr>
                <th>Userid</th>
                <th>Username</th>
                <th>Email</th>
                <th>Is Staff</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {users.map(u => (
                <tr key={u.Userid}>
                  <td>{u.Userid}</td>
                  <td>{u.username}</td>
                  <td>{u.email}</td>
                  <td>{u.is_staff ? 'Yes' : 'No'}</td>
                  <td>
                    <button
                      className="btn btn-warning mx-1"
                      onClick={() => navigate(`/users/edit/${u.Userid}`)}
                    >
                      Edit
                    </button>
                    <button
                      className="btn btn-danger mx-1"
                      onClick={() => handleDelete(u.Userid)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <p>No users available</p>
      )}
    </div>
  );
};

export default UsersPage;
