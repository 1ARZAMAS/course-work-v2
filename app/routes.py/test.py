from flask import Blueprint, render_template

test_bp = Blueprint('test', __name__)

@test_bp.route('/tests')
def tests():
    return render_template('test_page.html')
