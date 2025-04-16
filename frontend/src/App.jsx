import { Routes, Route } from 'react-router-dom';
import AppRoute from './utils/AppRoute';
import ScrollReveal from './utils/ScrollReveal';

// Layouts
import LayoutDefault from './layouts/LayoutDefault';
import LayoutAlternative from './layouts/LayoutAlternative';
import LayoutSignin from './layouts/LayoutSignin';

// Views 
import Home from './views/Home';
import Secondary from './views/Secondary';
import Login from './views/Login';
import Signup from './views/Signup';

const App = () => {
  return (
    <ScrollReveal>
      <Routes>
        <Route path="/" element={<AppRoute component={Home} layout={LayoutDefault} />} />
        <Route path="/secondary" element={<AppRoute component={Secondary} layout={LayoutAlternative} />} />
        <Route path="/login" element={<AppRoute component={Login} layout={LayoutSignin} />} />
        <Route path="/signup" element={<AppRoute component={Signup} layout={LayoutSignin} />} />
      </Routes>
    </ScrollReveal>
  );
};

export default App;
