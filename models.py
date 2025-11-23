from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    authors = db.Column(db.Text, nullable=False)  # JSON string
    abstract = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.Text)  # JSON string
    category = db.Column(db.String(50), nullable=False)
    pdf_path = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    citations = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'authors': json.loads(self.authors) if self.authors else [],
            'abstract': self.abstract,
            'keywords': json.loads(self.keywords) if self.keywords else [],
            'category': self.category,
            'pdf_path': self.pdf_path,
            'upload_date': self.upload_date.isoformat(),
            'views': self.views,
            'citations': self.citations
        }

    def __repr__(self):
        return f'<Article {self.title}>'