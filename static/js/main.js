// Main JavaScript file for search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const query = document.getElementById('searchQuery').value;
            const category = document.getElementById('categoryFilter').value;

            let url = '/api/search';
            const params = new URLSearchParams();

            if (query) params.append('q', query);
            if (category) params.append('category', category);

            url += '?' + params.toString();

            try {
                const response = await fetch(url);
                const articles = await response.json();

                const resultsDiv = document.getElementById('searchResults');
                resultsDiv.innerHTML = '';

                if (articles.length === 0) {
                    resultsDiv.innerHTML = '<p class="text-center text-muted">No articles found matching your search criteria.</p>';
                } else {
                    articles.forEach(article => {
                        const articleElement = createArticleCard(article);
                        resultsDiv.appendChild(articleElement);
                    });
                }
            } catch (error) {
                console.error('Error searching articles:', error);
            }
        });
    }

    // Also search on category change
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter) {
        categoryFilter.addEventListener('change', function() {
            document.getElementById('searchForm').dispatchEvent(new Event('submit'));
        });
    }
});

function createArticleCard(article) {
    const card = document.createElement('div');
    card.className = 'article-card';

    const formattedDate = new Date(article.upload_date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    const authors = Array.isArray(article.authors) ? article.authors.join(', ') : article.authors;
    const abstractPreview = article.abstract.length > 180
        ? article.abstract.substring(0, 180) + '...'
        : article.abstract;

    card.innerHTML = `
        <h3>${escapeHtml(article.title)}</h3>
        <div class="meta">
            <span>${escapeHtml(authors)}</span>
            <span>${formatCategory(article.category)}</span>
            <span>${formattedDate}</span>
        </div>
        <p class="abstract">${escapeHtml(abstractPreview)}</p>
        <a href="/article/${article.id}" class="read-more">Read more</a>
    `;

    return card;
}

function formatCategory(category) {
    const categories = {
        'philosophy': 'Philosophy',
        'history': 'History',
        'literature': 'Literature',
        'art-history': 'Art History',
        'cultural-studies': 'Cultural Studies',
        'linguistics': 'Linguistics',
        'religious-studies': 'Religious Studies',
        'classics': 'Classics',
        // Legacy categories for backward compatibility
        'computer-science': 'Computer Science',
        'biology': 'Biology',
        'physics': 'Physics',
        'chemistry': 'Chemistry',
        'mathematics': 'Mathematics',
        'medicine': 'Medicine',
        'engineering': 'Engineering',
        'social-sciences': 'Social Sciences'
    };
    return categories[category] || category.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
