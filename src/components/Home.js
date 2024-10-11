import axios from "axios";
import React, { useEffect, useState } from "react";
import '../styles/Home.css';
import { Link } from "react-router-dom";

function Home({ books }) {
  return (
    <div className="menuContainer">
      <h2>Welcome to our little library!</h2>
      <div className="menus">
        {books.map(book => (
          <div className="menu" key={book.id}>
            <h3>{book.title}</h3>
            {book.cover_image && <img src={book.cover_image} alt={book.title} />}
            <Link to={`/menu/${book.id}`}>
              <button>Read More</button>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
} 

export default Home;
