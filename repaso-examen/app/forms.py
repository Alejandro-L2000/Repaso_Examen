from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class HonorariosForm(FlaskForm):
    honorarios = DecimalField("Honorarios", validators=[DataRequired()])
    submit = SubmitField("Calcular")