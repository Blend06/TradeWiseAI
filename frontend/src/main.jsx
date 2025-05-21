import React from "react";
import { Navigation } from "../components/navigation";
import { Header } from "../components/header";
import { Features } from "../components/features";
import News from "../components/news";   
import { About } from "../components/about";
import Feedback from "../components/feedback"; 
import { Contact } from "../components/contact";
import JsonData from "../data/data.json";

const Main = () => {
  return (
    <div>
      <Navigation />
      <Header data={JsonData.Header} />
      <Features data={JsonData.Features} />
      <News />       
      <Feedback />   
      <About data={JsonData.About} />
      <Contact data={JsonData.Contact} />
    </div>
  );
};

export default Main;
