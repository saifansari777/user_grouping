from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from bson import ObjectId
from werkzeug.exceptions import abort

from .auth import login_required
from .db import init_db

bp = Blueprint('post', __name__)

@bp.route('/')
def index():
    db = init_db()
    posts = db.Post.find({})
    return render_template('post/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = init_db()
            db.Post.insert_one({"title":title, "content":content, "author_id":g.user["_id"]})
            return redirect(url_for('post.index'))

    return render_template('post/create.html')



def get_post(id, check_author=True):
    post = init_db().Post.find_one({"_id":ObjectId(id)})

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['_id']:
        abort(403)

    return post



@bp.route('/id/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = init_db()
            db.Post.update_one({"_id":ObjectId(id)}, {"$set" : {"title":title, "content":content} })
            
            return redirect(url_for('post.index'))

    return render_template('post/update.html', post=post)


@bp.route('/id/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = init_db()
    db.Post.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('blog.index'))