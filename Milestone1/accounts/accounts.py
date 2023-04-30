import math
import datetime
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sql.db import DB
from accounts.forms import CreateAccountForm
from werkzeug.datastructures import MultiDict
accounts = Blueprint('accounts', __name__, url_prefix='/accounts',template_folder='templates')

def refresh_account(account_id):
    b = DB.selectAll("SELECT SUM(balance_change) as balance FROM IS601_Transactions WHERE account_src=%s", account_id)
    balance = None
    if b.status and b.rows:
        balance = float(b.rows[0]['balance'])
    if balance != None:
        result = DB.insertOne("UPDATE IS601_Accounts set balance = %s WHERE id = %s",
                balance, account_id)
        return balance
    return None

def expected_balance_source(account_id, diff):
    b = DB.selectOne("SELECT * FROM IS601_Accounts WHERE id=%s LIMIT 1", account_id)
    
    expected_balance = 0.00
    if b.status and b.row:
        expected_balance = float(b.row['balance']) + diff
    return expected_balance

def expected_balance_dest(account_number, diff):
    b = DB.selectOne("SELECT * FROM IS601_Accounts WHERE account_number=%s LIMIT 1", account_number)
    
    expected_balance = 0.00
    if b.status and b.row:
        expected_balance = float(b.row['balance']) + diff
    return expected_balance

@accounts.route("/create", methods=["GET","POST"])
@login_required
def create():
    user_id = current_user.get_id()
    form = CreateAccountForm()  
    if form.validate_on_submit():
        try:

            result = DB.insertOne("INSERT INTO IS601_Accounts (account_type, balance, user_id) VALUES (%s, %s, %s)",
                form.acc_type.data, form.funds.data , user_id)

            # Option 2: Generate the number based on the id column;
            # requires inserting a null first to get the last insert id, then
            # update the record immediately after

            user_account = DB.selectOne("SELECT id FROM IS601_Accounts ORDER BY created DESC LIMIT 1")
            if user_account.status and user_account.row:
                user_account_id = user_account.row['id']
                acc_number = str(user_account_id).zfill(12)
                result = DB.insertOne("UPDATE IS601_Accounts set account_number = %s WHERE id = %s",
                acc_number, user_account_id)

            src_expected_total = expected_balance_source(1, form.funds.data*-1)
            trans1 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            1, user_account_id, form.funds.data*-1, src_expected_total, "Deposit", "")

            dst_expected_total = expected_balance_dest(acc_number, 0)
            trans2 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            user_account_id, 1, form.funds.data, dst_expected_total, "Deposit", "")

            refresh_account(1)
            refresh_account(user_account_id)

            if result.status:
                flash(f"Created {form.acc_type.data} account", "success")

            return redirect(url_for("accounts.list"))
        except Exception as e:
            flash(f"Error creating account - {e}", "danger")
    return render_template("account_form.html", form=form, type="Create")

@accounts.route("/list", methods=["GET"])
@login_required
def list():
    form = CreateAccountForm()
    return render_template("accounts_list.html")


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