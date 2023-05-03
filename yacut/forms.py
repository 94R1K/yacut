from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16), Optional(),
            Regexp(regex=r'^[a-zA-Z0-9]+$',
                   message='Указано недопустимое имя для короткой ссылки')
        ]
    )
    submit = SubmitField('Создать')
