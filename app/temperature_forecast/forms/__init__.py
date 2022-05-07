from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class weather_form(FlaskForm):
    city = TextAreaField('Enter City Name', [validators.DataRequired()])
    submit = SubmitField()