from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional

class EntryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[Optional()])
    title = StringField('Title', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[Optional()])
    submit = SubmitField('Submit')
