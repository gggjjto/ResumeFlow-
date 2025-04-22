import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ResumeGenerator from './pages/ResumeGenerator';
import './styles/global.css';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ResumeGenerator />} />
      </Routes>
    </Router>
  );
};

export default App;