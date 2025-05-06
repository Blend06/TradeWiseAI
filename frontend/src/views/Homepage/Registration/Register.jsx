import React, { useRef, useState } from 'react';
import axiosClient from '../../../utils/api';
import { useNavigate } from 'react-router-dom';
import './css/register.css';

const Register = () => {
  const nameRef = useRef();
  const emailRef = useRef();
  const passwordRef = useRef();
  const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const username = nameRef.current.value;
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    if (!passwordRegex.test(password)) {
      setErrorMessage(
        'Password must be at least 8 characters long and include both letters and numbers.'
      );
      return;
    }
    try {
      await axiosClient.post('/users/', { username, email, password });
      setErrorMessage('');
      setSuccessMessage('User registered successfully!');
      setTimeout(() => navigate('/login'), 1500);
    } catch (error) {
      setSuccessMessage('');
      setErrorMessage(
        error.response?.data?.error ||
        'An error occurred. Please try again.'
      );
    }
  };

  return (
    <section
      className="register-section"
      style={{
        padding: '20px',
        backgroundImage: 'url(/img/register.jpg)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        color: 'white',
      }}
    >
      <div className="wrapper">
        <div className="form-box">
          <div className="card-body">
            <h2 style={{ color: '#178ca4' }}>Register</h2>
            <form onSubmit={handleSubmit}>
              <div className="input-box mb-3">
                <input
                  ref={nameRef}
                  type="text"
                  className="form-control"
                  id="username"
                  placeholder="Username"
                  required
                />
              </div>
              <div className="input-box mb-3">
                <input
                  ref={emailRef}
                  type="email"
                  className="form-control"
                  id="email"
                  placeholder="Email"
                  required
                />
              </div>
              <div className="input-box mb-3">
                <input
                  ref={passwordRef}
                  type="password"
                  className="form-control"
                  id="password"
                  placeholder="Password"
                  required
                  onChange={() => setErrorMessage('')}
                />
              </div>
              <button
                type="submit"
                className="submit-button btn btn-primary w-100"
              >
                Register
              </button>
              {successMessage && (
                <p className="text-success mt-3 text-center">
                  {successMessage}
                </p>
              )}
              {errorMessage && (
                <p className="text-danger mt-3 text-center">
                  {errorMessage}
                </p>
              )}
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Register;
