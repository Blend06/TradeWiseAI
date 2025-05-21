import React, { useEffect, useState } from "react";
import axios from "axios";
import "./css/gallery.css";

const Feedback = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/userfeedback/")
      .then(({ data }) => {
        const sorted = data.sort(
          (a, b) => new Date(b.created_at) - new Date(a.created_at)
        );
        setFeedbacks(sorted.slice(0, 4));
      })
      .catch(() => setError("Failed to load feedbacks"))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div id="feedback" className="text-center mt-5">
      <div className="container">
        <div className="section-title">
          <h2>User Feedback</h2>
        </div>

        {loading && <p>Loading feedback...</p>}
        {error && <p className="text-danger">{error}</p>}

        <div className="gallery-items">
          {feedbacks.reduce((rows, feedback, index) => {
            if (index % 4 === 0) rows.push([]);
            rows[rows.length - 1].push(feedback);
            return rows;
          }, []).map((row, rowIndex) => (
            <div className="row" key={rowIndex}>
              {row.map((feedback) => (
                <div
                  className="col-12 col-sm-6 col-md-4 col-lg-3 p-2"
                  key={feedback.UserFeedbackId}
                >
                  <div className="card h-100">
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title text-capitalize">{feedback.feedback_type}</h5>
                      <p className="card-text flex-grow-1">{feedback.message}</p>
                      <p className="mb-1"><strong>Submitted by:</strong> {feedback.user?.username || "Anonymous"}</p>
                      <p className="text-muted" style={{ fontSize: "0.8rem" }}>
                        {new Date(feedback.created_at).toLocaleString()}
                      </p>
                    </div>
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

export default Feedback;
