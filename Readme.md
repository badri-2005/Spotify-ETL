# 🎧 Spotify ETL Project

This project performs an ETL (Extract, Transform, Load) operation using Spotify's API. It extracts track metadata from a list of Spotify track URLs, transforms the data into a structured format, and loads it into a MySQL database.

---

## 📌 Features

- ✅ Extracts track data (name, artist, album, popularity, duration) using the Spotify Web API  
- ✅ Parses URLs from a text file  
- ✅ Transforms and stores the data in a local MySQL database (`spotify_db`)  
- ✅ Uses `Spotipy`, a Python client for the Spotify Web API  
- ✅ Handles API errors and malformed URLs gracefully  

---

## 🔧 Tech Stack

- **Language:** Python 3.x  
- **Libraries:** 
  - `spotipy` (Spotify API)
  - `pandas` (optional for future extensions)
  - `re` (Regular Expressions)
  - `pymysql` (MySQL connection)
  - `matplotlib` (for future visualizations)  
- **Database:** MySQL  
- **API:** Spotify Web API  


