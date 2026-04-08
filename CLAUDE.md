# AI Assistant Context - Scholar Perspective

This file helps AI assistants understand the project context and decisions.

## Project Overview

Scholar Perspective is an academic journal website for liberal arts and humanities. The owner (choikyo) is building a professional platform to publish scholarly articles.

## Current Status

- **Local development:** Working
- **GitHub:** https://github.com/choikyo/ScholarPerspective
- **Hosting:** PythonAnywhere ($10/mo Web Developer plan)
- **Domain:** www.scholarperspective.com (live — DNS via domain.com, CNAME → PythonAnywhere)

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
- Uses **PDF.js** (CDN) to render PDFs as canvas elements — no iframe
- All pages rendered, fits screen width, sharp on Retina/HiDPI displays (devicePixelRatio aware)
- Copy protection: right-click disabled, keyboard shortcuts blocked (Ctrl/Cmd+C/A/X/S/P)
- Fixed back button (←) floats on left side of screen while reading
- Route: `/publications/view/<filepath>`

### Future Considerations (discussed but not implemented)
- Database for articles (3-5 years out)
- Nightly batch DOCX → PDF conversion

## File Locations

| Purpose | Location |
|---------|----------|
| Article PDFs | `articles/[Issue Name]/*.pdf` |
| Article metadata | `articles/articles.csv` |
| Book cover image | `static/images/cover.png` |
| Logo (white) | `static/images/logo.png` |
| Main styles | `static/css/style.css` |

## Navigation Structure

- Home (`/`) - Hero section + contact form (functional, sends email via Gmail SMTP)
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
