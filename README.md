cat > README.md <<'EOL'
# HackerNews Scraper Dashboard

A full-stack dashboard that fetches and displays real-time Hacker News headlines using Python Flask and ReactJS.

## Overview
- Scrapes latest headlines from Hacker News.
- Displays them in a clean ReactJS frontend.
- Backend fetches data using Python, BeautifulSoup, and Flask.
- Frontend updates automatically by calling the local API.

## How to Run Locally

### Backend
\`\`\`bash
cd backend
python -m venv venv        # optional, create virtual env
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python api.py
\`\`\`
- Backend runs at: http://localhost:5000

### Frontend
\`\`\`bash
cd frontend
npm install
npm start
\`\`\`
- Frontend runs at: http://localhost:3000

## Usage
- Open the frontend URL in a browser to see live Hacker News headlines.
- Clicking a headline will take you to the original Hacker News page.

## Why it works
- The Flask backend scrapes data from Hacker News and provides it through an API.
- The React frontend fetches this API data in real-time and displays it interactively.
- Fully functional locally without deployment.

## Author
Pramath Hegde
EOL

echo "✅ README.md created successfully!"
