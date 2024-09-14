from flask import Blueprint, render_template

bp = Blueprint('modalities', __name__, url_prefix='/modalities')

@bp.route('/')
def index():
    # TODO: Fetch AI modalities from database
    modalities = []
    return render_template('modalities.html', modalities=modalities)

@bp.route('/<modality>')
def modality(modality):
    # TODO: Fetch specific modality information
    modality_info = {}
    return render_template('modality_detail.html', modality=modality_info)

# Add a new route for use cases of modalities
@bp.route('/<modality>/use-cases')
def modality_use_cases(modality):
    # TODO: Fetch use cases for the specific modality
    use_cases = []
    return render_template('modality_use_cases.html', modality=modality, use_cases=use_cases)