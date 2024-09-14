# Import your forms here

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

class ToolForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    features = StringField('Features')
    pricing = StringField('Pricing')
    website = StringField('Website', validators=[URL(message="Please enter a valid URL")])
    submit = SubmitField('Submit')