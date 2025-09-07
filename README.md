# 1️⃣ Navigate to project folder
cd C:/Desktop/PROJECTS/news-scraper || { echo "Project folder not found!"; exit 1; }

# 2️⃣ Remove any embedded Git repos (if needed)
rm -rf frontend/.git
rm -rf backend/.git

# 3️⃣ Initialize git if not already
git init

# 4️⃣ Create a clean README.md
cat > README.md <<'EOL'
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
news-scraper/
│
├── backend/ # Flask backend
│ ├── api.py # Main API file
│ ├── scraper.py # Scraper logic
│ ├── requirements.txt # Python dependencies
│
├── frontend/ # ReactJS frontend
│ ├── src/ # React components and CSS
│ ├── public/ # HTML and assets
│ └── package.json # React dependencies & scripts
│
└── README.md # Project documentation

text

---

## Installation & Run Locally

### Backend
cd backend
python -m venv venv # optional, create virtual env
venv\Scripts\activate # activate on Windows
pip install -r requirements.txt
python api.py

text
The backend runs on: http://localhost:5000

### Frontend
cd frontend
npm install
npm start

text
The frontend runs on: http://localhost:3000

Open in your browser and see Hacker News headlines.

---

## Usage
- The React frontend fetches live headlines from your local Flask backend.
- Clicking a headline will take you to the original Hacker News page.

---

## Notes
- Currently works locally; deployment is optional.
- For real-time remote usage, deploy the backend and update the frontend API URL.

---

## Author
Pramath Hegde
EOL

# 5️⃣ Add all files to git
git add .

# 6️⃣ Commit changes
git commit -m "Add HackerNews Scraper Dashboard project with backend and frontend"

# 7️⃣ Set remote origin (replace URL if needed)
git remote add origin https://github.com/pramathhegde/HackerNews-Scraper-Dashboard.git

# 8️⃣ Push to GitHub
git branch -M main
git push -u origin main --force

echo "✅ Project files and README pushed to GitHub successfully!"
