# ⚽ Football Data Scraping with Selenium

A Python web scraping project that extracts football match data from [adamchoi.co.uk](https://www.adamchoi.co.uk/teamgoals/detailed) using Selenium.

## ✨ Features
- Scrapes match data (date, home team, score, away team)
- Supports filtering by country via dropdown
- Exports data to CSV

## 📦 Requirements
- Python 3.x · Google Chrome · ChromeDriver
  ```
  pip install selenium pandas
  ```

## 🚀 Setup
1. Download [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version
2. Update the `path` variable in `project.py` with your ChromeDriver path
3. Run: `python project.py`

## 📊 Output
`matches_data.csv` — contains the following columns:

| Column | Description |
|---|---|
| date | Match date |
| home_team | Home team name |
| score | Match score |
| away_team | Away team name |

## 🛠️ Tech Stack
- [Selenium](https://www.selenium.dev/) — browser automation
- [Pandas](https://pandas.pydata.org/) — data manipulation & CSV export
