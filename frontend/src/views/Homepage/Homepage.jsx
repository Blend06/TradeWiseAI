import React from "react";
import { Navigation } from "../../components/navigation";
import { Header } from "../../components/header";
import { Features } from "../../components/features";
import { About } from "../../components/about";
import  Feedback  from "../../components/feedback";
import { News } from "../../components/news";
import { Contact } from "../../components/contact";

const Homepage = () => {
  return (
    <div>
      <Navigation />
      <Header />
      <Features />
      <News />
      <Feedback />
      <About />
      <Contact />
    </div>
  );
};

export default Homepage;
