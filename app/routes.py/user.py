from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/home')
@login_required
def home():
    return render_template('home_page.html', user=current_user)
