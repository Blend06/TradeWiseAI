import React from 'react';
import PropTypes from 'prop-types';
import { throttle } from 'lodash';


class ScrollReveal extends React.Component {
  state = {
    viewportHeight: window.innerHeight,
    revealEl: []
  };

  // Check if all elements have been revealed
  checkComplete = () => {
    return this.state.revealEl.length <= document.querySelectorAll('[class*=reveal-].is-revealed').length;
  };

  // Check if the element is visible in the viewport
  elementIsVisible = (el, offset) => {
    return el.getBoundingClientRect().top <= this.state.viewportHeight - offset;
  };

  // Reveal elements when they come into view
  revealElements = () => {
    if (this.checkComplete()) return;
    
    for (let i = 0; i < this.state.revealEl.length; i++) {
      let el = this.state.revealEl[i];
      let revealDelay = el.getAttribute('data-reveal-delay');
      let revealOffset = el.getAttribute('data-reveal-offset') || 200;
      
      // Ensure that the closest method uses a valid selector string, not an element
      let revealContainerSelector = el.getAttribute('data-reveal-container') || el;
      let listenedEl = revealContainerSelector instanceof HTMLElement 
        ? revealContainerSelector 
        : el.closest(revealContainerSelector);

      if (this.elementIsVisible(listenedEl, revealOffset) && !el.classList.contains('is-revealed')) {
        if (revealDelay) {
          setTimeout(() => {
            el.classList.add('is-revealed');
          }, revealDelay);
        } else {
          el.classList.add('is-revealed');
        }
      }
    }
  };

  // Initialize the component, set up elements to reveal
  init = () => {
    setTimeout(() => {
      this.setState({ revealEl: document.querySelectorAll('[class*=reveal-]') }, () => {
        if (!this.checkComplete()) {
          window.addEventListener('scroll', this.handleScroll);
          window.addEventListener('resize', this.handleResize);
        }
        this.revealElements();
      });
    }, 100);
  };

  // Remove event listeners once all elements have been revealed
  handleListeners = () => {
    if (this.checkComplete()) {
      window.removeEventListener('scroll', this.handleScroll);
      window.removeEventListener('resize', this.handleResize);
    }
  };

  // Throttled scroll handler
  handleScroll = throttle(() => {
    this.handleListeners();
    this.revealElements();
  }, 30);

  // Throttled resize handler
  handleResize = throttle(() => {
    this.setState({ viewportHeight: window.innerHeight }, () => {
      this.handleListeners();
      this.revealElements();
    });
  }, 30);

  // ComponentDidMount lifecycle method
  componentDidMount() {
    this.init();
  }

  render() {
    return <>{this.props.children}</>;
  }
}

ScrollReveal.propTypes = {
  children: PropTypes.node.isRequired,
};

export default ScrollReveal;
