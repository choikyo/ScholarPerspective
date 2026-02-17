# AI Assistant Context - Scholar Perspective

This file helps AI assistants understand the project context and decisions.

## Project Overview

Scholar Perspective is an academic journal website for liberal arts and humanities. The owner (choikyo) is building a professional platform to publish scholarly articles.

## Current Status

- **Local development:** Working
- **GitHub:** https://github.com/choikyo/ScholarPerspective
- **Hosting:** PythonAnywhere (free tier for testing, plan to upgrade to $10/mo)
- **Domain:** www.scholarperspective.com (owned, currently on GoDaddy, to be migrated)

## Key Design Decisions

### UI/Design
- Dark header (`#1a1a2e`) to display white logo
- Periwinkle blue accent (`#5B7FD3`) from logo
- Serif fonts (Georgia) for headings - academic feel
- Sans-serif for body text - readability

### Article Management
- PDFs stored in `articles/[Issue Name]/` folders
- Metadata stored in `articles/articles.csv` (not database)
- CSV format: `issue,filename,title,authors`
- Authors with commas need double quotes: `"Author One, Author Two"`

### PDF Viewer
- Copy protection enabled (CSS user-select, JS keyboard blocking)
- Uses iframe with `#toolbar=0` to hide PDF toolbar
- Route: `/publications/view/<filepath>`

### Future Considerations (discussed but not implemented)
- Database for articles (3-5 years out)
- Nightly batch DOCX → PDF conversion
- Contact form functionality (currently non-functional placeholder)

## File Locations

| Purpose | Location |
|---------|----------|
| Article PDFs | `articles/[Issue Name]/*.pdf` |
| Article metadata | `articles/articles.csv` |
| Book cover image | `static/images/book_cover.jpg` |
| Logo (white) | `static/images/logo.png` |
| Main styles | `static/css/style.css` |

## Navigation Structure

- Home (`/`) - Hero section + contact form placeholder
- View Publications (`/publications`) - Issue list with articles
- Board of Members (`/board`) - Editorial board page

## Commands

```bash
# Run locally
python app.py

# Push to GitHub
git add -A && git commit -m "message" && git push

# Update PythonAnywhere (in PA console)
cd ~/ScholarPerspective && git pull
# Then click Reload on Web tab
```

## Owner Preferences

- Prefers simple solutions over complex ones
- CSV over database for now (easy to edit)
- Wants copy protection on articles
- Academic/professional aesthetic
