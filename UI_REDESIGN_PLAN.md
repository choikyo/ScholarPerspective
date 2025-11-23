# UI Redesign Action Plan
## ScholarPerspective - Professional Academic Journal Interface

---

## Overview

Redesign the interface to be clean, modern, and professional — suitable for a liberal arts academic publication. Design harmonizes with the existing periwinkle blue geometric logo.

---

## Design System

### Colors (Derived from Logo)
```
Primary Accent:    #5B7FD3  (periwinkle blue - matches logo)
Primary Hover:     #4A6BC2  (darker blue for interactions)
Background:        #ffffff  (white)
Surface:           #f8f9fc  (light blue-tinted gray for cards)
Text Primary:      #1a1a2e  (deep navy for headings)
Text Secondary:    #4a4a5a  (dark gray for body)
Text Muted:        #6e6e7a  (gray for metadata)
Border:            #e1e4ed  (cool light gray)
```

### Typography
- **Headings**: Georgia (serif) — scholarly, academic feel
- **Body**: System sans-serif — clean readability
- **Line height**: 1.6-1.8 for comfortable reading

---

## Action Items (In Sequence)

### Step 1: Rewrite `static/css/style.css`

**What changes:**
- [ ] Update color variables to match logo palette
- [ ] Change heading fonts to Georgia (serif)
- [ ] Remove heavy box-shadows, use subtle borders instead
- [ ] Increase whitespace/padding throughout
- [ ] Simplify navigation styling (no blue button, text links only)
- [ ] Clean form input styles with periwinkle focus ring
- [ ] Refine article cards (subtle border, no shadow)
- [ ] Update button styles (rounded, periwinkle blue)
- [ ] Improve responsive breakpoints

---

### Step 2: Update `templates/base.html`

**What changes:**
- [ ] Simplify navigation structure
- [ ] Keep logo image + "Scholar Perspective" text
- [ ] Update nav links: Home, View Publications, Search
- [ ] Remove "Submit Your Article" button (redundant)
- [ ] Add subtle bottom border to header instead of shadow

**Before:**
```html
<nav>
    <div class="logo">
        <img src="..." alt="ScholarPerspective">
        Scholar Perspective
    </div>
    <ul>
        <li><a href="...">Home</a></li>
        <li><a href="...">View Publications</a></li>
        <li><a href="...">Search</a></li>
        <li><a href="#" class="submit-btn">Submit Your Article</a></li>
    </ul>
</nav>
```

**After:**
```html
<nav>
    <a href="/" class="logo">
        <img src="..." alt="">
        <span>Scholar Perspective</span>
    </a>
    <ul class="nav-links">
        <li><a href="...">Home</a></li>
        <li><a href="...">View Publications</a></li>
        <li><a href="...">Search</a></li>
    </ul>
</nav>
```

---

### Step 3: Update `templates/index.html`

**What changes:**
- [ ] Simplify hero section layout
- [ ] Update headline text for liberal arts focus
- [ ] Clean up contact section styling
- [ ] Remove placeholder image reference or update it

**Hero content focus:**
- Headline: "Advancing Scholarship in Arts & Humanities"
- Subtext emphasizing liberal arts academic publishing

---

### Step 4: Update `templates/search.html`

**What changes:**
- [ ] Center the search form
- [ ] Style search input cleanly (larger, rounded)
- [ ] Style category dropdown to match
- [ ] Update results grid styling

---

### Step 5: Update `templates/upload.html`

**What changes:**
- [ ] Update form styling for cleaner appearance
- [ ] Improve spacing between form groups
- [ ] Style file input more elegantly
- [ ] Update submit button styling

---

### Step 6: Update `templates/article.html`

**What changes:**
- [ ] Use serif font for article title
- [ ] Clean metadata section styling
- [ ] Improve abstract readability (max-width for text)
- [ ] Style download button to match new design

---

### Step 7: Update `static/js/main.js`

**What changes:**
- [ ] Update dynamically generated article card HTML to match new CSS classes (if any class names change)

---

## Visual Reference

### Navigation (After)
```
┌────────────────────────────────────────────────────────────────────┐
│  [Logo] Scholar Perspective              Home  View Publications  Search  │
├────────────────────────────────────────────────────────────────────┤
```

### Article Card (After)
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Article Title Here (Georgia, serif)                          │
│   Author Name  •  Social Sciences  •  January 15, 2025         │
│                                                                 │
│   Abstract text preview displayed here in a comfortable        │
│   sans-serif font for easy reading...                          │
│                                                                 │
│   Read more →                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Search Page (After)
```
                    Search Publications

        ┌─────────────────────────────────────┐
        │  Search by title, author, keyword   │
        └─────────────────────────────────────┘
                 [ All Categories ▼ ]
                     [ Search ]
```

---

## Verification Checklist

After implementation, verify:

- [ ] Run `python app.py` and open http://localhost:5000
- [ ] Homepage loads with clean styling
- [ ] Navigation links work correctly
- [ ] Logo displays properly in header
- [ ] Search page functions and displays results
- [ ] Upload form submits correctly
- [ ] Article detail page displays properly
- [ ] Responsive design works on mobile (resize browser)
- [ ] All colors match the logo's periwinkle blue

---

## Notes

- No external CSS frameworks (keeping vanilla CSS)
- No external fonts loaded (using system fonts for performance)
- Maintaining all existing functionality
- Only updating visual presentation
