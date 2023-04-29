import math
import datetime
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sql.db import DB
from accounts.forms import CreateAccountForm
from werkzeug.datastructures import MultiDict
accounts = Blueprint('accounts', __name__, url_prefix='/accounts',template_folder='templates')

@accounts.route("/create", methods=["GET","POST"])
@login_required
def create():
    form = CreateAccountForm() 
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/list", methods=["GET"])
@login_required
def list():
    form = CreateAccountForm()
    return render_template("accounts_list.html")

@accounts.route("/transactions", methods=["GET"])
@login_required
def transactions():
    return render_template("transactions_list.html", rows=rows, pages=pages, current_page=page, account=account)

@accounts.route("/deposit", methods=["GET","POST"])
@login_required
def deposit():
    return render_template("deposit_withdraw_form.html", form=form, type="Deposit")

@accounts.route("/withdraw", methods=["GET","POST"])
@login_required
def withdraw():
    return render_template("deposit_withdraw_form.html", form=form, type="Withdraw")

@accounts.route("/transfer", methods=["GET","POST"])
@login_required
def transfer():
    return render_template("transfer_form.html", form=form)

@accounts.route("/profile", methods=["GET","POST"])
@login_required
def ext_transfer():
    return render_template("profile.html", form=form)