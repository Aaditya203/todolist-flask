from .forms import Registration,LoginForm
from flask import Blueprint,render_template,url_for,flash,redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,logout_user,login_user,login_required
from ..models import Users
from .. import db

auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/',methods=["GET","POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # to check if email already exists or not 
        user = Users.query.filter_by(email=email).first()
        if user:
            flash("User Already Exists!","danger")
            return render_template("register.html")
        
        # generate hash password
        hashed_password = generate_password_hash(password)
        new_user = Users(name=name,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html",form=form)

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('task.view_task'))
        else:
            flash("Invalid Credentials!","danger")
    return render_template("login.html",form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
