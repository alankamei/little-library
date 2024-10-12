import React from 'react';
import { Link } from 'react-router-dom';
import SearchIcon from '@mui/icons-material/Search';
import '../styles/Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">Logo</div>
      <div className="search-container">
        <input className="search-input" placeholder='Search books' />
        <SearchIcon className="search-icon" />
      </div>
      <div className="nav-links">
        <Link className="nav-link" to='/login'>Login</Link>
        <Link className="nav-link" to='/register'>Register</Link>
      </div>
    </nav>
  );
}

export default Navbar;
