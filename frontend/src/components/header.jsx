import React from "react";
import PropTypes from "prop-types";

export const Header = ({ data }) => {
  return (
    <header id="header" role="banner">
      <div className="intro">
        <div className="overlay">
          <div className="container">
            <div className="row">
              <div className="col-md-8 col-md-offset-2 intro-text">
                <h1>
                Empower Your Future. Invest in Crypto.
                  <span></span>
                </h1>
                <p>
                Explore the world of decentralized finance and digital assets. Take control of your wealth, embrace innovation, and be part of the financial revolution — start your crypto journey today.
                </p>
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

// PropTypes to validate props
Header.propTypes = {
  data: PropTypes.shape({
    paragraph: PropTypes.string,
  }),
};


Header.defaultProps = {
  data: {
    paragraph:
      "Discover the perfect blend of comfort, elegance, and timeless fashion.",
  },
};
