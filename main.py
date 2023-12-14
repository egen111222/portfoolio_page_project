from flask import Flask,render_template
from models import db
from models import Blog
from dotenv import load_dotenv
import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blog_part import blog_app

load_dotenv()

app = Flask(__name__,
            static_url_path="")
app.secret_key=os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]

db.init_app(app)
with app.app_context():
    db.create_all()
    
@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(blog_app,url_prefix="/blog")

admin = Admin(app, name='Сайт Нашого Блогу', template_mode='bootstrap3')
admin.add_view(ModelView(Blog, db.session))

if __name__ == "__main__":
    app.run()
