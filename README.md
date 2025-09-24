# 🐦 Flask Twitter Clone

A mini Twitter-like web app built with **Flask**, **SQLAlchemy**, and **Jinja templates**.  
Users can register, log in, and post/edit tweets.  

---

## 📌 Features
- 🔑 User authentication (register & login)
- 📝 Create, edit, and delete tweets
- 🏷️ Categories for tweets
- 📄 Simple and clean UI with custom CSS/JS
- 💾 SQLite database (can be switched to MySQL/Postgres)

---

## 📂 Project Structure
twitter/
│── app/
│ ├── routes/ # Flask blueprints (auth & tweets)
│ ├── static/ # JS & CSS files
│ ├── templates/ # HTML templates
│ ├── models.py # Database models
│ └── init.py # App factory
│── instance/ # Local DB (ignored by git)
│── run.py # Entry point

---


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayushWeb07/flask-sql.git
cd flask-sql

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Rum the app
python run.py

---

## 🛠️ Tech Stack

- **Backend:** Flask, SQLAlchemy
    
- **Frontend:** HTML, CSS, JS (Jinja2 templates)
    
- **Database:** SQLite (default)
    

---

## 📸 Screenshots

![Login](/assets/about.png)
![Home](/assets/home.png)
![Categories](/assets/categories.png)
![About](/assets/about.png)


