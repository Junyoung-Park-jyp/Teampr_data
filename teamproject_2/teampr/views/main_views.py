from flask import Blueprint, render_template
from teampr.models import *
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    wine_list = WineData.query.order_by(WineData.price.desc())
    return render_template("index.html", wine_list = wine_list)
    # 데이터 조회 예시: 모든 데이터를 가져오는 경우
    # wine_list = WineData.query.all()
    # data_list = [{'id': item.ID} for item in data]

    return data_list
@bp.route('/search', methods=["POST"]) 
def search():
    filter_data = request.join
    filtered_wines = WineData
    if filter_data.get("wine_type"):
        filtered_wines = [wine for wine in filtered_wines if wine['wine_type'] in filter_data['wine_type']]
    return 'Search'

