import React, { useEffect, useState } from 'react';
import axiosClient from '../../../utils/api';
import { useNavigate } from 'react-router-dom';

const UserFeedbackPage = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    axiosClient.get('/userfeedback/')
      .then(({ data }) => setFeedbacks(data))
      .catch(() => setError('Failed to load feedbacks'))
      .finally(() => setLoading(false));
  }, []);

  const handleDelete = async id => {
    if (!window.confirm('⚠️ Are you sure you want to delete this feedback?')) return;
    try {
      await axiosClient.delete(`/userfeedback/${id}/`);
      setFeedbacks(feedbacks.filter(fb => fb.FeedbackId !== id));
    } catch {
      alert('Failed to delete feedback');
    }
  };

  if (loading) return <div>Loading feedbacks…</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-primary">User Feedback Management</h1>

      <button className="btn btn-primary mb-3" onClick={() => navigate('/userfeedback/new')}>
        Submit New Feedback
      </button>

      {feedbacks.length > 0 ? (
        <div className="table-responsive">
          <table className="table table-bordered table-striped">
            <thead>
              <tr>
                <th>Feedback ID</th>
                <th>User</th>
                <th>Feedback</th>
                <th>Submitted At</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {feedbacks.map(fb => (
                <tr key={fb.UserFeedbackId}>
                  <td>{fb.UserFeedbackId}</td>
                  <td>{fb.user}</td>
                  <td>{fb.message}</td>
                  <td>{fb.feedback_type}</td>
                  <td>
                    <button
                      className="btn btn-warning mx-1"
                      onClick={() => navigate(`/userfeedback/edit/${fb.FeedbackId}`)}
                    >
                      Edit
                    </button>
                    <button
                      className="btn btn-danger mx-1"
                      onClick={() => handleDelete(fb.FeedbackId)}
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
        <p>No feedback available</p>
      )}
    </div>
  );
};

export default UserFeedbackPage;
