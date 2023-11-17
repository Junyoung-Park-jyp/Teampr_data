from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    low = 50000
    medium = 100000
    high = 150000
    CATEGORIES = [('Red wine', '레드 와인'), ('White wine', '화이트 와인')]
    PRICES = [(low, '5만원 이하'), (medium, '10만원 이하'), (high, '15만원 이하')]
    RATINGS = [(4, '별점 4'), (3.5, '별점 3.5'), (3, '별점 3')]

    categories = SelectMultipleField('와인 종류', choices=CATEGORIES, option_widget=widgets.CheckboxInput())
    prices = SelectMultipleField('가격대', choices=PRICES, option_widget=widgets.CheckboxInput())
    ratings = SelectMultipleField('별점', choices=RATINGS, option_widget=widgets.CheckboxInput())