# Go to your project folder
cd C:/Desktop/PROJECTS/news-scraper

# Create README.md
cat > README.md <<EOL
# HackerNews Scraper Dashboard

A full-stack dashboard that fetches and displays real-time Hacker News headlines using Python Flask and ReactJS.

---

## Features
- Scrapes latest headlines from [Hacker News](https://news.ycombinator.com/)
- Displays headlines in a clean ReactJS frontend
- Fully functional locally without deployment

---

## Tech Stack
- **Backend:** Python, Flask, BeautifulSoup, Requests
- **Frontend:** ReactJS, HTML, CSS
- **Other Tools:** Flask-CORS

---

## Project Structure
\`\`\`
news-scraper/
│
├── backend/               # Flask backend
│   ├── api.py             # Main API file
│   ├── scraper.py         # Scraper logic
│   ├── requirements.txt   # Python dependencies
│
├── frontend/              # ReactJS frontend
│   ├── src/               # React components and CSS
│   ├── public/            # HTML and assets
│   └── package.json       # React dependencies & scripts
│
└── README.md              # Project documentation
\`\`\`

---

## Installation & Run Locally

### Backend
\`\`\`bash
cd backend
python -m venv venv        # optional, create virtual env
venv\Scripts\activate      # activate on Windows
pip install -r requirements.txt
python api.py
\`\`\`
- The backend runs on: \`http://localhost:5000\`

### Frontend
\`\`\`bash
cd frontend
npm install
npm start
\`\`\`
- The frontend runs on: \`http://localhost:3000\`
- Open in your browser and see Hacker News headlines.

---

## Usage
- The React frontend fetches live headlines from your local Flask backend
- Clicking a headline will take you to the original Hacker News page

---

## Notes
- Currently works locally; deployment is optional
- For real-time remote usage, deploy the backend and update the frontend API URL

---

## Author
Pramath Hegde
EOL

# Add README to git
git add README.md

# Commit changes
git commit -m "Add README for HackerNews Scraper Dashboard"

# Push to GitHub
git push origin main
