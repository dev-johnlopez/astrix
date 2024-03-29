# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from app.extensions import login_manager
from app.public.forms import LoginForm, ContactForm
from app.user.forms import RegisterForm
from app.user.models import User
from app.utils import flash_errors, flash_success
from app.emails import send_new_contact_form_email

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)

@blueprint.route("/contact", methods=["GET", "POST"])
def contact():
    """Home page."""
    form = ContactForm()
    current_app.logger.info("Hello from the contact page!")
    # Handle logging in
    if request.method == "POST":
        current_app.logger.info("POSTING!")
        if form.validate_on_submit():
            current_app.logger.info("SUCCESS!")
            current_app.logger.info("SUCCESS!")
            current_app.logger.info("SUCCESS!")
            current_app.logger.info("SUCCESS!")
            current_app.logger.info("SUCCESS!")
            send_new_contact_form_email(form)
            flash_success("We received your message!")
        else:
            flash_errors(form)
    return render_template("public/contact.html", form=form)

@blueprint.route("/demo", methods=["GET", "POST"])
def demo():
    return render_template("public/demo.html")


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
