from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Gym


class GymForm(FlaskForm):
    task = StringField('Task',
        validators = [
            DataRequired(),
        ]    
    )
    submit = SubmitField('Submit')

    def validate_task(self, task):
        Gym = Gym.query.all()
        for gym in gym:
            if gym.task == task.data:
                raise ValidationError('You already added this Exercise')

class OrderGym(FlaskForm):
    order_with = SelectField('Order With',
        choices=[
            ("complete", "Completed"),
            ("id", "Recent"),
            ("old", "Old"),
            ('incomplete', "Incomplete")
        ]
    )
    submit = SubmitField('Order')