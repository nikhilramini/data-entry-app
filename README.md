# Data Entry Web App

This is a Flask-based web application for entering and managing data records.

##  Technologies Used
- Python 3
- Flask
- Flask-WTF
- SQLite (via SQLAlchemy)
- HTML/CSS (Jinja2 templates)

##  Installation

```bash
git clone https://github.com/nikhilramini/data-entry-app.git
cd data-entry-app
pip install -r requirements.txt

# Run the Flask application:
export FLASK_APP=app.py           # On Windows use `set FLASK_APP=app.py`
export FLASK_ENV=development      # On Windows use `set FLASK_ENV=development`
flask run

Open your browser and navigate to the URL displayed in the terminal after running flask run

Usage
Fill in the form fields and submit.

Required fields are Name and Title, you will see errors if these are left blank.

After submitting, you will be redirected to a confirmation page showing your entry and all previous entries.