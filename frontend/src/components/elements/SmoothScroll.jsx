import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';

const propTypes = {
  children: PropTypes.node,
  to: PropTypes.string.isRequired,
  duration: PropTypes.number,
  onLinkClick: PropTypes.func,
};

class SmoothScroll extends React.Component {

  // Easing function
  easeInOutQuad = (t) => {
    return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
  };

  // Scroll logic for custom smooth scrolling
  scrollToEl = (startTime, currentTime, duration, scrollEndElemTop, startScrollOffset) => {
    const runtime = currentTime - startTime;
    let progress = runtime / duration;

    progress = Math.min(progress, 1);
    const ease = this.easeInOutQuad(progress);

    window.scroll(0, startScrollOffset + (scrollEndElemTop * ease));

    if (runtime < duration) {
      window.requestAnimationFrame((timestamp) => {
        const currentTime = timestamp || new Date().getTime();
        this.scrollToEl(startTime, currentTime, duration, scrollEndElemTop, startScrollOffset);
      });
    }
  };

  // Smooth scroll handler
  smoothScroll = (e) => {
    e.preventDefault();

    const { to, duration, onLinkClick } = this.props;
    const target = document.getElementById(to);

    if (!target) return;

    // Call the onLinkClick prop if provided
    if (onLinkClick) {
      onLinkClick();
    }

    // Check if the browser supports native smooth scrolling
    if ('scrollBehavior' in document.documentElement.style) {
      target.scrollIntoView({ behavior: 'smooth' });
    } else {
      // Fall back to custom smooth scrolling logic
      window.requestAnimationFrame((timestamp) => {
        const start = timestamp || new Date().getTime();
        const startScrollOffset = window.pageYOffset;
        const scrollEndElemTop = target.getBoundingClientRect().top;

        this.scrollToEl(start, start, duration || 1000, scrollEndElemTop, startScrollOffset);
      });
    }
  };

  render() {
    const { className, children, to, duration, onLinkClick, ...props } = this.props;

    const classes = classNames(
      className
    );

    return (
      <a
        {...props}
        className={classes}
        href={'#' + to}
        onClick={this.smoothScroll}
        aria-label={`Scroll to ${to}`}
      >
        {children}
      </a>
    );
  }
}

SmoothScroll.propTypes = propTypes;
SmoothScroll.defaultProps = {
  duration: 1000,
  onLinkClick: null,
};

export default SmoothScroll;
