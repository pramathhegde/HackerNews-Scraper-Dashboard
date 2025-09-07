

# Go to project folder
cd C:/Desktop/PROJECTS/news-scraper

# Create a simple README.md
cat > README.md <<'EOL'
# HackerNews Scraper Dashboard

A full-stack dashboard that fetches and displays real-time Hacker News headlines using Python Flask and ReactJS.

## Overview
- Scrapes latest headlines from Hacker News.
- Displays them in a clean, interactive ReactJS frontend.
- Backend fetches data using Python, BeautifulSoup, and Flask.
- Frontend updates automatically by calling the local API.

## How it works
1. The Flask backend runs a scraper (`scraper.py`) that fetches the latest headlines.
2. An API endpoint (`api.py`) serves these headlines in JSON format.
3. The ReactJS frontend fetches this JSON and displays the headlines in the browser.

## Why it’s useful
- Quickly see trending news from Hacker News in one dashboard.
- Learn how to integrate web scraping with a frontend UI.
- Works fully locally without needing deployment.

## Author
Pramath Hegde
EOL

# Add all files to git
git add .

# Commit
git commit -m "Add simplified README for HackerNews Scraper Dashboard"

# Push to GitHub
git remote add origin https://github.com/pramathhegde/HackerNews-Scraper-Dashboard.git
git branch -M main
git push -u origin main --force

echo "✅ Simplified README pushed successfully!"
