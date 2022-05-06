from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, BooleanField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from app.headphones.models import Headphone

class AddHeadphoneForm(FlaskForm):
    brand_id = SelectField('Brand', coerce=int, validators=[DataRequired()])
    type_id = SelectField('Type', coerce=int, validators=[DataRequired()])
    color_id = SelectField('Color', coerce=int, validators=[DataRequired()])
    image_id = SelectField('Image(name)', coerce=int, validators=[DataRequired()])
    model_name = StringField('Model', validators=[DataRequired()])
    price = IntegerField('Price(USD)', validators=[DataRequired()])
    lifetime = IntegerField('Life time(h)', validators=[DataRequired()])
    max_power = IntegerField('Max power(Hz)', validators=[DataRequired()])
    weight = IntegerField('Weight(g)', validators=[DataRequired()])
    impedance = IntegerField('Impedance(Ohm)', validators=[DataRequired()])
    sensitivity = IntegerField('Sensitivity(dB)', validators=[DataRequired()])
    lifetime_case = IntegerField('Case life time(h)', validators=[DataRequired()])
    is_nc = BooleanField('Noise reduction')
    is_deleted = BooleanField('Deleted')
    submit = SubmitField('Add in the database!')

    def validate_model_name(self, model_name):
        name_headphone = Headphone.query.filter_by(model_name=model_name.data).first()
        if name_headphone is not None:
            raise ValidationError('This model is already in the database.')
            