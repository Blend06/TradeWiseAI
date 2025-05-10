import React, { useEffect, useState } from 'react';
import axiosClient from '../../../utils/api';
import { useNavigate } from 'react-router-dom';

const NewsPage = () => {
  const [News, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    axiosClient.get('/newsarticle/')
      .then(({ data }) => setNews(data))
      .catch(() => setError('Failed to load News data'))
      .finally(() => setLoading(false));
  }, [navigate]);

  const handleDelete = async NewsArticleId => {
    
    if (!window.confirm('⚠️ Are you sure you want to delete this news?')) 
      return;
    
    try {
      await axiosClient.delete(`/newsarticle/${NewsArticleId}/`);
      setNews(News.filter(u => u.NewsArticleId !== NewsArticleId));
    } catch {
      alert('Failed to delete news');
    }
  };

  if (loading) return <div>Loading News…</div>;
  if (error)   return <div>{error}</div>;

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 fw-bold text-danger">Manage News</h1>

      <button className="btn btn-primary mb-3" onClick={() => navigate('/news/new')}>
        Create New News
      </button>

      {News.length > 0 ? (
        <div className="table-responsive">
          <table className="table table-bordered table-striped">
            <thead>
              <tr>
                <th>NewsArticleid</th>
                <th>title</th>
                <th>content</th>
                <th>image</th>
                <th>published_at</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {News.map(u => (
                <tr key={u.NewsArticleId}>
                  <td>{u.NewsArticleId}</td>
                  <td>{u.title}</td>
                  <td>{u.content}</td>
                  <td>{u.image}</td>
                  <td>{u.published_at}</td>
                  <td>
                    <button
                      className="btn btn-warning mx-1"
                      onClick={() => navigate(`/News/edit/${u.NewsArticleId}`)}
                    >
                      Edit
                    </button>
                    <button
                      className="btn btn-danger mx-1"
                      onClick={() => handleDelete(u.NewsArticleId)}
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
        <p>No News available</p>
      )}
    </div>
  );
};

export default NewsPage;
