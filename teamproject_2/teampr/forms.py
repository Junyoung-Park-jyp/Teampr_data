from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    wine_type = SelectMultipleField('와인 종류', choices=[
        ('red', '레드 와인'),
        ('white', '화이트 와인')
    ])

    price = SelectMultipleField('가격대', choices=[
        ('low', '5만원 이하'),
        ('medium', '10만원 이하'),
        ('high', '15만원 이하')
    ], validators=[DataRequired()])

    score = SelectMultipleField('별점', choices=[
        ('4', '별점 4점 이상'),
        ('3.5', '별점 3.5점 이상'),
        ('3', '별점 3점 이상')
    ], validators=[DataRequired()])

class WhiskeyForm(FlaskForm):
    volume = SelectMultipleField('용량', choices=[
        ('500', '500ml 이상'),
        ('1000', '1000ml 이상')
    ])

    price = SelectMultipleField('가격대', choices=[
        ('low', '20만원 이하'),
        ('medium', '50만원 이하'),
        ('high', '제한 없음')
    ], validators=[DataRequired()])

    year = SelectMultipleField('숙성 기간', choices=[
        ('10', '10년 이상'),
        ('15', '15년 이상'),
        ('20', '20년 이상')
    ], validators=[DataRequired()])

