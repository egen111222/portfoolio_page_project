from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(250))
    text = db.Column(db.Text)
