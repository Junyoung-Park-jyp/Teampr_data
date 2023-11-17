from datetime import datetime
from flask import Blueprint, render_template, request, url_for, session
from teampr.models import *
from teampr.forms import *
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    wine_list = WineData.query.order_by(WineData.price.desc())
    
    return render_template("index.html", wine_list = wine_list)



@bp.route('/search/', methods=('GET', 'POST'))
def search():
    form = FilterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # db.session.commit()
        session['filtered_data'] = {
            'wine_type': form.wine_type.data,
            'price': form.price.data,
            'score': form.score.data
        }
        return redirect(url_for('main.result'))
    return render_template('search/category.html', form = form)

@bp.route('/search/result/', methods=('GET', 'POST'))
def result():
    filtered_data = session.get('filtered_data')
    wine_type = "Red wine" if filtered_data.get('wine_type') == 'red' else "White wine"
    price = 50000 if filtered_data.get('price') == 'low' else (100000 if filtered_data.get('price') == 'medium' else 150000)
    score = 3.0 if filtered_data.get('score') == '3' else (3.5 if filtered_data.get('score') == '3.5' else 4.0)
    filtered_wines = WineData.query.filter_by(wine_type=wine_type)\
                                .filter(WineData.price <= price)\
                                .filter(WineData.score <= score)\
                                .all()

    return render_template('search/result.html', filtered_wines=filtered_wines)