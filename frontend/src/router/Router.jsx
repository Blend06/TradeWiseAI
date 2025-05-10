import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Homepage from "../views/Homepage/Homepage";
import Login from "../views/Homepage/Registration/Login";
import Register from "../views/Homepage/Registration/Register";
import ControlPanel from "../views/controlpanel/ControlPanel";
import UsersPage from "../views/controlpanel/Users/UsersPage";
import UsersForm from "../views/controlpanel/Users/UsersForm";
import NewsPage from "../views/controlpanel/News/NewsPage";
import NewsForm from "../views/controlpanel/News/NewsForm";

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        {/* Home, Login, Register */}
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/controlpanel" element={<ControlPanel />} />
        <Route path="/users"               element={<UsersPage />} />
        <Route path="/users/new"           element={<UsersForm />} />
        <Route path="/users/edit/:userId"  element={<UsersForm />} />
        <Route path="/news"               element={<NewsPage />} />
        <Route path="/news/new"           element={<NewsForm />} />
        <Route path="/news/edit/:NewsArticleId"  element={<NewsForm />} />
        

      </Routes>
    </Router>
  );
};

export default AppRouter;
