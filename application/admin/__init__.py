from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime
from application.core.orderservice import get_order_yesterday_today_statistic
from application.core.userservice import get_bot_users_yesterday_today_statistic
bp = Blueprint('admin', __name__)

from application.admin import users, orders, orders_map, catalog, administrator, settings, comments, requests, excel


@bp.context_processor
def view_context_processor():
    return {
        'year': datetime.now().year
    }


@bp.route('/', methods=['GET', 'HEAD'])
@login_required
def index():
    return render_template('admin/index.html')
