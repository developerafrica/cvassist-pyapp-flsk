from flask import Blueprint, render_template, request, flash, redirect, url_for
from api.models.usersmodel import Users
from api import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint("auth", __name__, url_prefix="/auth")


def validate(name, email, password, confirm):
    if len(name) < 2:
        flash("enter a valid name ! : names must contain more than 2 charecters", category="error")
        return False
    elif len(email) < 4:
        flash("enter a valid email account", category="error")
        return False
    elif password != confirm:
        flash("passwords provided do not match", category="error")
        return False
    elif len(password) < 6:
        flash("password must have at least 7 charecters", category="error")
        return False
    else:
        flash("account created", category="sucess")
        return True


@auth.route("/signup", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
              
        if validate(name, email, password, confirm) == True:
            create_user = Users(name=name, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(create_user)
            db.session.commit()
            login_user(create_user, remember=True)
            return redirect(url_for("ui.profile"))
        
        

    return render_template("signup.html", user=current_user)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("logged in sucessfully", category='sucess')
                return redirect(url_for("ui.profile"))
            else:
                flash("incorect password", category='error')


    return render_template("login.html", user=current_user)


@auth.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("ui.index"))