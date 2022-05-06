from flask import Blueprint, render_template

from app.headphones.models import Headphone

blueprint = Blueprint('main', __name__, url_prefix='/')

def get_catalog_headphones():
    headphones = Headphone.query.order_by(Headphone.model_name).all()
    return headphones


@blueprint.route('/index')
def index_page():
    headphones = get_catalog_headphones()
    title = "Wireless headphones"
    return render_template('index.html', page_title=title, headphones=headphones)
    