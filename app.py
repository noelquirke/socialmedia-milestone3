import models
import forms
from flask import Flask, g, render_template, flash, url_for, redirect, abort # noqa
from flask_bcrypt import check_password_hash # noqa
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user, AnonymousUserMixin # noqa
lm = LoginManager

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'noelquirke900@hotmail.com'


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.anonymous_user = Anonymous


@login_manager.user_loader
def load_user(userId):
    try:
        return models.User.get(models.User.id == userId)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    "" "Connect to the database before each request" ""
    if not hasattr(g, 'db'):
        g.db = models.DATABASE
        g.db.connect()
        g.user = current_user
    # g.db = models.DATABASE
    # if g.db.is_closed():
    #     g.db.connect()


@app.after_request
def after_request(response):
    """ We close the connection to the database """
    g.db.close()
    return response


@app.route("/post/<int:post_id>")
def view_post(post_id):
    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    return render_template('stream.html', stream=posts)


@app.route('/follow/<username>')
@login_required
def follow(username):
    try:
        to_user = models.User.get(models.User.username ** username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.create(from_user=g.user._get_current_object(), to_user=to_user) # noqa
        except models.IntegrityError:
            pass
        else:
            flash('Now you follow {}'.format(to_user.username), "success")
    return redirect(url_for('stream', username=to_user.username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    try:
        to_user = models.User.get(models.User.username ** username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.get(from_user=g.user._get_current_object(), to_user=to_user).delete_instance() # noqa
        except models.IntegrityError:
            pass
        else:
            flash('You stopped following {}'.format(to_user.username), "success") # noqa
    return redirect(url_for('stream', username=to_user.username))


@app.route("/register", methods=("GET", "POST"))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash('User register!!!', 'success')
        models.User.create_user(username=form.username.data, email=form.email.data, password=form.password.data) # noqa
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash('Username or password does not exist', 'danger')
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print(user)
                flash(" you're logged in ", 'success')
                return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out", 'success')
    return redirect(url_for('index'))


@app.route("/new_post", methods=("GET", "POST"))
def posts():
    form = forms.PostsForm()
    if form.validate_on_submit():
        models.Post.create(user=g.user._get_current_object(), content=form.content.data.strip()) # noqa
        flash("Posted Message", "success")
        return redirect(url_for("index"))
    return render_template("post.html", form=form)


@app.route('/')
def index():
    stream = models.Post.select().limit(100)
    return render_template('stream.html', stream=stream)

# All the posts that the current user is following


@app.route('/stream')
@app.route('/stream/<username>')
def stream(username=None):
    template = 'stream.html'
    if username and username != current_user.username:
        try:
            user = models.User.select().where(models.User.username**username).get() # noqa
        except models.DoesNotExist:
            abort(404)
        else:
            stream = user.posts.limit(100)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'user_stream.html'
    return render_template(template, stream=stream, user=user)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(username="Noel", email="noelquirke900@hotmail.com", password="12345") # noqa
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
