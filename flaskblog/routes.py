import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog.forms import UpdateAccountForm, PostForm
from flaskblog.models import Post
from flaskblog import app
from flaskblog import db
from flask_login import logout_user, current_user, login_required
from flaskblog.infrastructure.controller import user_controller


@app.route('/home')
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about this flask blog')


@app.route('/register', methods=['GET', 'POST'])
def register():
    controller = user_controller()
    return controller.register()


@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = user_controller()
    return controller.login()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture) -> str:
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f'{random_hex}{f_ext}'
    picture_path = os.path.join(app.root_path, 'static', 'profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    if i.mode == "P":
        if 'transparency' in i.info:
            i = i.convert('RGBA')
        else:
            i = i.convert('RGB')

    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    image_file = url_for('static', filename=f'profile_pics/{current_user.image_file}')
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.__session.commit()
        flash('Your account have been updated successfully', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Your account', form=form, picture=image_file)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.__session.add(post)
        db.__session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='Create post')


@app.route('/post/<int:post_id>')
def post(post_id: int):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id: int):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    form.title.data = post.title
    form.content.data = post.content
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.__session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    return render_template('create_post.html', title='Update Post', form=form, legend='Update post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id: int):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.__session.delete(post)
    db.__session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))
