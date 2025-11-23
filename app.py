from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import db, Article
from config import Config
import os
import json
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    return app

app = create_app()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    articles = Article.query.order_by(Article.upload_date.desc()).limit(10).all()
    return render_template('index.html', articles=articles)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if file is present
        if 'pdf' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['pdf']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Create article record
            article = Article(
                title=request.form.get('title'),
                authors=json.dumps(request.form.getlist('authors')[0].split(',')),
                abstract=request.form.get('abstract'),
                keywords=json.dumps(request.form.get('keywords', '').split(',')),
                category=request.form.get('category'),
                pdf_path=filepath
            )
            
            db.session.add(article)
            db.session.commit()
            
            flash('Article uploaded successfully!')
            return redirect(url_for('index'))
        else:
            flash('Only PDF files are allowed')
    
    return render_template('upload.html')

@app.route('/api/articles', methods=['GET'])
def api_articles():
    articles = Article.query.order_by(Article.upload_date.desc()).all()
    return jsonify([article.to_dict() for article in articles])

@app.route('/api/articles/<int:article_id>', methods=['GET'])
def api_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.views += 1
    db.session.commit()
    return jsonify(article.to_dict())

@app.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    
    articles_query = Article.query
    
    if query:
        articles_query = articles_query.filter(
            db.or_(
                Article.title.contains(query),
                Article.abstract.contains(query),
                Article.authors.contains(query)
            )
        )
    
    if category:
        articles_query = articles_query.filter(Article.category == category)
    
    articles = articles_query.order_by(Article.upload_date.desc()).all()
    return jsonify([article.to_dict() for article in articles])

@app.route('/search')
def search_page():
    return render_template('search.html')

@app.route('/publications')
def publications():
    """List all issues and their articles from the articles folder."""
    articles_dir = os.path.join(app.root_path, 'articles')
    issues = []

    if os.path.exists(articles_dir):
        # Get all issue folders, sorted
        issue_folders = sorted([f for f in os.listdir(articles_dir)
                               if os.path.isdir(os.path.join(articles_dir, f)) and not f.startswith('.')])

        for issue_name in issue_folders:
            issue_path = os.path.join(articles_dir, issue_name)
            # Get all article files in this issue
            article_files = sorted([f for f in os.listdir(issue_path)
                                   if os.path.isfile(os.path.join(issue_path, f)) and not f.startswith('.')])
            issues.append({
                'name': issue_name,
                'articles': article_files
            })

    return render_template('publications.html', issues=issues)

@app.route('/publications/view/<path:filepath>')
def view_article(filepath):
    """View article PDF in browser without allowing copy/paste."""
    articles_dir = os.path.join(app.root_path, 'articles')
    file_path = os.path.join(articles_dir, filepath)

    if not os.path.exists(file_path):
        flash('Article not found')
        return redirect(url_for('publications'))

    # Extract filename for display
    filename = os.path.basename(filepath)
    issue_name = os.path.dirname(filepath)

    # Get article title (filename without extension)
    article_title = os.path.splitext(filename)[0]

    return render_template('article_viewer.html',
                         title=article_title,
                         issue=issue_name,
                         filepath=filepath)

@app.route('/publications/pdf/<path:filepath>')
def serve_pdf(filepath):
    """Serve PDF file for viewing."""
    from flask import send_from_directory
    articles_dir = os.path.join(app.root_path, 'articles')
    return send_from_directory(articles_dir, filepath)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    article.views += 1
    db.session.commit()
    return render_template('article.html', article=article)

@app.route('/api/upload', methods=['POST'])
def api_upload():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Parse authors and keywords
        authors_data = request.form.get('authors', '[]')
        keywords_data = request.form.get('keywords', '[]')
        
        try:
            authors = json.loads(authors_data) if authors_data.startswith('[') else authors_data.split(',')
            keywords = json.loads(keywords_data) if keywords_data.startswith('[') else keywords_data.split(',')
        except:
            authors = authors_data.split(',')
            keywords = keywords_data.split(',')
        
        article = Article(
            title=request.form.get('title'),
            authors=json.dumps([a.strip() for a in authors]),
            abstract=request.form.get('abstract'),
            keywords=json.dumps([k.strip() for k in keywords]),
            category=request.form.get('category'),
            pdf_path=filepath
        )
        
        db.session.add(article)
        db.session.commit()
        
        return jsonify({'message': 'Article uploaded successfully', 'article': article.to_dict()}), 201
    else:
        return jsonify({'error': 'Only PDF files are allowed'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)