import React, { useEffect, useState } from "react";

function App() {
  const [headlines, setHeadlines] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/headlines")
      .then(res => res.json())
      .then(data => setHeadlines(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ backgroundColor: "#111", color: "#fff", minHeight: "100vh", padding: "2rem" }}>
      <h1 style={{ fontSize: "2rem", marginBottom: "1.5rem" }}>📰 Hacker News Headlines</h1>
      <div style={{ maxWidth: "800px", margin: "auto" }}>
        {headlines.map(h => (
          <div key={h.id} style={{ backgroundColor: "#222", padding: "1rem", marginBottom: "1rem", borderRadius: "8px" }}>
            <a href={h.link} target="_blank" rel="noopener noreferrer" style={{ fontSize: "1.1rem", color: "#4dabf7", textDecoration: "none" }}>
              {h.title}
            </a>
            <p style={{ fontSize: "0.8rem", color: "#aaa" }}>Scraped at: {h.scraped_at}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
