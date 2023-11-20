from datetime import datetime
from flask import Blueprint, render_template, request, url_for, session
from teampr.models import *
from teampr.forms import *
from werkzeug.utils import redirect
from sqlalchemy import or_
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    wine_list = WineData.query.order_by(WineData.price.desc())
    
    return render_template("index.html", wine_list = wine_list)
@bp.route('/refers')
def refers():
    return render_template("refers.html")


@bp.route('wine/search/', methods=('GET', 'POST'))
def wine_search():
    form = FilterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # db.session.commit()
        session['wine_filtered_data'] = {
            'wine_type': "Red wine" if form.wine_type.data[0] == 'red' else 'White wine',
            'price': 50000 if form.price.data[0] == 'low' else (100000 if form.price.data[0] == 'medium' else 150000),
            'score': 3.0 if form.score.data[0] == '3' else (3.5 if form.score.data[0] == '3.5' else 4.0)
        }
        return redirect(url_for('main.wine_result'))
    return render_template('search/wine_category.html', form = form)

@bp.route('whiskey/search/', methods=('GET', 'POST'))
def whiskey_search():
    form = WhiskeyForm()
    if request.method == 'POST' and form.validate_on_submit():
        # db.session.commit()
        session['whiskey_filtered_data'] = {
            'volume': 500 if form.volume.data[0] == '500' else 1000,
            'price': 200000 if form.price.data[0] == 'low' else (500000 if form.price.data[0] == 'medium' else 2000000),
            'year': 10 if form.year.data[0] == '10' else (15 if form.year.data[0] == '15' else 20)
        }
        return redirect(url_for('main.whiskey_result'))
    return render_template('search/whiskey_category.html', form = form)

@bp.route('beer/search/', methods=('GET', 'POST'))
def beer_search():

    return render_template('index.html')

@bp.route('non_alcohol/search/', methods=('GET', 'POST'))
def non_alcohol_search():

    return render_template('index.html')

@bp.route('wine/search/result/', methods=('GET', 'POST'))
def wine_result():
    wine_filtered_data = session.get('wine_filtered_data')
    wine_type = wine_filtered_data.get("wine_type")
    price = wine_filtered_data.get('price')
    score = wine_filtered_data.get('score')
    filtered_wines = WineData.query.filter(
        WineData.price <= price,
        WineData.wine_type == wine_type,
        WineData.score >= score
    ).all()

    return render_template('search/wine_result.html', filtered_wines=filtered_wines, wine_filter = session.get('wine_filtered_data'))

@bp.route('whiskey/search/result/', methods=('GET', 'POST'))
def whiskey_result():
    whiskey_filtered_data = session.get('filtered_data')
    volume = whiskey_filtered_data.get("volume")
    price = whiskey_filtered_data.get('price')
    year = whiskey_filtered_data.get('year')
    filtered_whiskeys = Whiskey.query.filter(or_(
        Whiskey.volume.isnot(None),
        Whiskey.price.isnot(None),
        Whiskey.year.isnot(None)
        ),
        Whiskey.price <= price,
        Whiskey.volume >= volume,
        Whiskey.year >= year
    ).all()

    return render_template('search/whiskey_result.html',filtered_whiskeys=filtered_whiskeys, whiskey_filter = session.get('whiskey_filtered_data'))
