# Scholar Perspective

A professional academic journal website for arts and humanities research.

## Tech Stack

- **Backend:** Flask (Python 3.10)
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Hosting:** PythonAnywhere
- **Version Control:** GitHub

## Project Structure

```
ScholarPerspective/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── articles/              # PDF articles organized by issue
│   ├── articles.csv       # Article metadata (title, authors)
│   └── Issue 1 - 2026-Feb/
│       └── *.pdf
├── static/
│   ├── css/style.css      # Main stylesheet
│   ├── js/main.js         # JavaScript (search functionality)
│   └── images/            # Logo, book covers
└── templates/
    ├── base.html          # Base template with navigation
    ├── index.html         # Homepage
    ├── publications.html  # Publications listing
    ├── article_viewer.html # PDF viewer with copy protection
    ├── board.html         # Board of Members page
    └── search.html        # Search page
```

## Setup

### Local Development

```bash
# Clone repository
git clone https://github.com/choikyo/ScholarPerspective.git
cd ScholarPerspective

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

Visit `http://127.0.0.1:5000`

### PythonAnywhere Deployment

1. Clone repo in PythonAnywhere Bash console
2. Create virtualenv: `mkvirtualenv --python=/usr/bin/python3.10 scholarvenv`
3. Install requirements: `pip install -r requirements.txt`
4. Configure Web app with manual Flask setup
5. Set WSGI file to import `app` from `app.py`

## Adding New Articles

1. Add PDF file to appropriate issue folder in `articles/`
2. Add entry to `articles/articles.csv`:
   ```csv
   Issue Name,filename.pdf,Article Title,"Author One, Author Two"
   ```
3. Commit and push to GitHub
4. Pull on PythonAnywhere and reload

## Key Features

- **Publications Browser:** Expandable issue list with article metadata
- **PDF Viewer:** In-browser viewing with copy protection
- **Responsive Design:** Mobile-friendly layout
- **Dark Header:** Designed for white logo visibility

## Domain

- Production: www.scholarperspective.com (to be configured)
- Current: [username].pythonanywhere.com

## License

All rights reserved. Scholar Perspective © 2025
