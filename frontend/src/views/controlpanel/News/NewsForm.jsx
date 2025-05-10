import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axiosClient from '../../../utils/api';

const NewsForm = () => {
  const { NewsArticleId } = useParams();
  const navigate = useNavigate();

  const [NewsArticleData, setNewsArticleData] = useState({
    title: '',
    content: '',
    image: null,
    published_at: ''
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!NewsArticleId) return;
    setLoading(true);
    axiosClient.get(`/newsarticle/${NewsArticleId}/`)
      .then(({ data: NewsArticle }) => {
        setNewsArticleData({
          title: NewsArticle.title,
          content: NewsArticle.content,
          image: null,  // Don't preload image file
          published_at: NewsArticle.published_at,
        });
      })
      .catch(() => setError('Failed to load NewsArticle details'))
      .finally(() => setLoading(false));
  }, [NewsArticleId, navigate]);

  const handleChange = e => {
    const { name, type, files, value, checked } = e.target;
    setNewsArticleData(prev => ({
      ...prev,
      [name]: type === 'file' ? files[0] : type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);

    try {
      const formData = new FormData();
      for (const key in NewsArticleData) {
        if (NewsArticleData[key] !== null) {
          formData.append(key, NewsArticleData[key]);
        }
      }

      if (NewsArticleId) {
        await axiosClient.patch(`/newsarticle/${NewsArticleId}/`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
        alert('NewsArticle updated successfully!');
      } else {
        await axiosClient.post('/newsarticle/', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
        alert('NewsArticle created successfully!');
      }

      navigate('/news');
    } catch (err) {
      console.error(err);
      setError('Failed to save NewsArticle');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading…</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-danger">
        {NewsArticleId ? 'Edit NewsArticle' : 'Create NewsArticle'}
      </h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="title">Title</label>
          <input
            id="title"
            name="title"
            type="text"
            className="form-control"
            value={NewsArticleData.title}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="content">Content</label>
          <input
            id="content"
            name="content"
            type="text"
            className="form-control"
            value={NewsArticleData.content}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="image">Image</label>
          <input
            id="image"
            name="image"
            type="file"
            accept="image/*"
            className="form-control"
            onChange={handleChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          {NewsArticleId ? 'Update NewsArticle' : 'Create NewsArticle'}
        </button>
      </form>
    </div>
  );
};

export default NewsForm;
