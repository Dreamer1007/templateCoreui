from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils  import secure_filename


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/NewModal")
def NewModal():
    return render_template("newModal.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/register.html", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('blank'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('preview'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('preview'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/preview.html")
def preview():
    return render_template('preview.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/blank.html")
def blank():
    return render_template('blank.html')

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')



@app.route('/CreateModal', methods = ['GET', 'POST'])
def CreateModal():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return request.form.get('input')
      return request.form.get('output')
