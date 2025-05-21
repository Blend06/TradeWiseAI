import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, Link } from "react-router-dom";
import axiosClient from "../utils/api";

export const Navigation = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    if (!token) return;

    axiosClient
      .get("/users/me/")
      .then((res) => {
        setUser(res.data);
      })
      .catch((err) => {
        console.error("Error fetching user info:", err);
      });
  }, []);

  if (location.pathname === "/login" || location.pathname === "/register") {
    return null;
  }

  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    setUser(null);
    navigate("/");
  };

  return (
    <nav id="menu" className="navbar navbar-default navbar-fixed-top" style={{ minHeight: "50px", marginLeft: 0, marginRight: 0 }}>
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: 0 }}>
        <Link className="navbar-brand page-scroll" to="/" style={{ margin: 0, padding: "14px 0", fontWeight: 600, letterSpacing: "0.5px" }}>
          LuxuryStep
        </Link>
        <div style={{ display: "flex", alignItems: "center" }}>
          <ul className="nav navbar-nav" style={{ marginBottom: 0, display: "flex", alignItems: "center" }}>
            <li><a href="#features" className="page-scroll" style={{ padding: "10px 15px" }}>Features</a></li>
            <li><a href="#news" className="page-scroll" style={{ padding: "10px 15px" }}>News</a></li>
            <li><a href="#feedback" className="page-scroll" style={{ padding: "10px 15px" }}>Feedback</a></li>
            <li><a href="#about" className="page-scroll" style={{ padding: "10px 15px" }}>About</a></li>
            {user ? (
              <>
                <li>
                  <Link to="/cart" className="page-scroll" style={{ padding: "10px 15px", fontSize: "20px", display: "flex", alignItems: "center" }}>
                    <i
                      className="bi bi-cart-fill"
                      aria-label="Shopping Cart"
                      onMouseEnter={() => setIsHovered(true)}
                      onMouseLeave={() => setIsHovered(false)}
                      style={{ fontSize: "24px", color: isHovered ? "orange" : "#333", padding: "10px", transition: "color 0.3s" }}
                    />
                  </Link>
                </li>
                <li>
                  <Link to="/addtowishlist" className="page-scroll" style={{ padding: "10px 15px", color: "grey" }}>
                    <i
                      className="bi bi-heart"
                      aria-label="Wishlist"
                      onMouseEnter={() => setIsHovered(true)}
                      onMouseLeave={() => setIsHovered(false)}
                      style={{ fontSize: "24px", color: isHovered ? "red" : "#333", padding: "10px", transition: "color 0.3s" }}
                    />
                  </Link>
                </li>
                <li>
                  <button
                    onClick={handleLogout}
                    style={{ color: "#333", border: "1px solid #ccc", borderRadius: "4px", padding: "5px 12px", fontSize: "14px", backgroundColor: "#fff", cursor: "pointer", marginLeft: "20px" }}
                  >
                    LOGOUT
                  </button>
                </li>
                {user.is_staff && (
                  <li>
                    <button
                      onClick={() => navigate("/controlpanel")}
                      className="btn btn-danger"
                      style={{ color: "#fff", fontSize: "14px", padding: "5px 12px", cursor: "pointer", marginLeft: "15px" }}
                    >
                      Control Panel
                    </button>
                  </li>
                )}
              </>
            ) : (
              <li style={{ marginLeft: "20px", display: "flex", gap: "10px" }}>
                <Link to="/login" style={{ textDecoration: "none", color: "#333", border: "1px solid #ccc", borderRadius: "4px", padding: "5px 12px", fontSize: "14px", backgroundColor: "#fff" }}>
                  LOGIN
                </Link>
                <Link to="/register" style={{ textDecoration: "none", color: "#333", border: "1px solid #ccc", borderRadius: "4px", padding: "5px 12px", fontSize: "14px", backgroundColor: "#fff" }}>
                  REGISTER
                </Link>
              </li>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};
