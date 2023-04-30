import datetime
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField, DateField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class CreateAccountForm(FlaskForm):
    acc_type_choices = [('Checking', 'Checking Account'), ('Savings', 'Savings Account'), ('Fixed Deposit', 'Fixed Deposit Account'), ('Money Market', 'Money Market Account'), ('Certificates of Deposit', 'Certificates of Deposit Account')]
    acc_type = SelectField("Account Type", choices=acc_type_choices, validators=[DataRequired()])
    funds = FloatField("Initial Deposit funds", validators=[InputRequired(),NumberRange(min=5)])
    submit = SubmitField("Create")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)