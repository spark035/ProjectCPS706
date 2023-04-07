from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class EdgeInputForm(FlaskForm):
    vert1 = StringField('V1', validators=[DataRequired])
    vert2 = StringField('V2', validators=[DataRequired])
    weight = IntegerField('Weight', validators=[DataRequired])
    submit = SubmitField('Add edge')