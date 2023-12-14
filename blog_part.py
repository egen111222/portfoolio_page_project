from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from models import Blog

blog_app = Blueprint('blog_app', __name__,
                     template_folder='templates')

@blog_app.route("/")
def view_blogs():
    blogs = Blog.query.all()
    return render_template("blogs.html",
                           blogs=blogs)

@blog_app.route("/<int:blog_id>")
def view_blog(blog_id):
    pass
