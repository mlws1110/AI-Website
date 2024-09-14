from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/ai-boom')
def ai_boom():
    return render_template('ai_boom.html')

# Add a new route for privacy policy
@bp.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

# Add a new route for terms of service
@bp.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')