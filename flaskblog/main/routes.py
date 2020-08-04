from flask import Blueprint
from flask import render_template, request

from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)


'''
route is what we type in the browser to go to differents pages 
'''


@main.route('/about')
def about_page():
    return render_template('403.html', title='About')

