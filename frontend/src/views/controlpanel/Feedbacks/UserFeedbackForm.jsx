import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axiosClient from '../../../utils/api';

const UserFeedbackForm = () => {
  const { FeedbackId } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    user: '',
    message: '',
    feedback_type: '',
  });

  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const feedbackChoices = [
    { value: 'suggestion', label: 'Suggestion' },
    { value: 'problem', label: 'Problem' },
    { value: 'comment', label: 'Comment' },
  ];

  // Load users for the dropdown
  useEffect(() => {
    axiosClient.get('/users/')
      .then(({ data }) => setUsers(data))
      .catch(() => setError('Failed to load users'));
  }, []);

  // Load feedback if editing
  useEffect(() => {
    if (!FeedbackId) return;
    setLoading(true);
    axiosClient.get(`/userfeedback/${FeedbackId}/`)
      .then(({ data }) => {
        setFormData({
          user: data.user,
          message: data.message,
          feedback_type: data.feedback_type,
        });
      })
      .catch(() => setError('Failed to load feedback'))
      .finally(() => setLoading(false));
  }, [FeedbackId]);

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    try {
      if (FeedbackId) {
        await axiosClient.patch(`/userfeedback/${FeedbackId}/`, formData);
        alert('Feedback updated successfully!');
      } else {
        await axiosClient.post('/userfeedback/', formData);
        alert('Feedback submitted successfully!');
      }
      navigate('/userfeedback');
    } catch (err) {
      console.error(err);
      setError('Failed to save feedback');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading…</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-primary">
        {FeedbackId ? 'Edit Feedback' : 'Submit Feedback'}
      </h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="user">User</label>
          <select
            id="user"
            name="user"
            className="form-control"
            value={formData.user}
            onChange={handleChange}
            required
          >
            <option value="">Select a user</option>
            {users.map(user => (
              <option key={user.Userid} value={user.Userid}>
                {user.username || user.email}
              </option>
            ))}
          </select>
        </div>
        <div className="mb-3">
          <label htmlFor="message">Message</label>
          <textarea
            id="message"
            name="message"
            className="form-control"
            value={formData.message}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="feedback_type">Feedback Type</label>
          <select
            id="feedback_type"
            name="feedback_type"
            className="form-control"
            value={formData.feedback_type}
            onChange={handleChange}
            required
          >
            <option value="">Select feedback type</option>
            {feedbackChoices.map(choice => (
              <option key={choice.value} value={choice.value}>
                {choice.label}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" className="btn btn-success">
          {FeedbackId ? 'Update Feedback' : 'Submit Feedback'}
        </button>
      </form>
    </div>
  );
};

export default UserFeedbackForm;
