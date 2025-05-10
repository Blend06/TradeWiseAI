import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

 import axios from 'axios';
import "./css/gallery.css";

export const News = () => {
   const [NewsArticle, setNewsArticle] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();


useEffect(() => {
  axios.get('http://localhost:8000/api/newsarticle/')
    .then(({ data }) => setNewsArticle(data))
    .catch(() => setError('Failed to load News data'))
    .finally(() => setLoading(false));
}, []);

  return (
    <div id="portfolio" className="text-center">
      <div className="container">
        <div className="section-title">
          <h2>News Articles</h2>
        </div>
        <div className="gallery-items">
          {NewsArticle.reduce((rows, NewsArticle, index) => {
            if (index % 4 === 0) rows.push([]);
            rows[rows.length - 1].push(NewsArticle);
            return rows;
          }, []).map((row, rowIndex) => (
            <div className="row" key={rowIndex}>
              {row.map((NewsArticle) => (
                <div
                  className="col-12 col-sm-6 col-md-4 col-lg-3 p-2"
                  key={NewsArticle.NewsArticleId}
                >
                  <div className="NewsArticle-card">
                    <div className="NewsArticle-image">
                     <img
  src={
    NewsArticle.image.startsWith("http")
      ? NewsArticle.image
      : `http://localhost:8000${NewsArticle.image}`
  }
  alt={NewsArticle.title}
  style={{ width: "100px", height: "100px", objectFit: "cover" }}
/>
                     
                    </div>
                    <h4>{NewsArticle.title}</h4>
                    <p>{NewsArticle.content}</p>
                    <p><strong>Date published: {NewsArticle.published_at}</strong></p>
                    

                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
  
};

export default News;
