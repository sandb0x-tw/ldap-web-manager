from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    vue_content = render_template('views/login.vue')
    return render_template('main.html', content=vue_content)
