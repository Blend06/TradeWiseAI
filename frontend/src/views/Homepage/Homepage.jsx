import React from "react";
import { Navigation } from "../../components/navigation";
import { Header } from "../../components/header";
import { Features } from "../../components/features";
import { About } from "../../components/about";
import { Services } from "../../components/services";
import { Contact } from "../../components/contact";
import { News } from "../../components/news";


const Homepage = () => {
  
 

  return (
    <div>
      <Navigation />
      <Header />
      <Features />
      <News />
      <Services />

      <About />
      <Contact />
    </div>
  );
};

export default Homepage;
