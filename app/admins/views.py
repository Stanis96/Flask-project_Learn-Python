from flask import Blueprint, render_template

from app.users.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/')

@blueprint.route('/')
@admin_required
def admin_index():
    title = 'Tool bar'
    return render_template('admin.html', page_title=title)
