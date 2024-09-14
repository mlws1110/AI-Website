from flask import Blueprint, render_template, request
from app.models.tool import Tool

bp = Blueprint('tools', __name__, url_prefix='/tools')

@bp.route('/')
def index():
    tools = Tool.query.filter(Tool.category != 'LLM').all()
    llms = Tool.query.filter(Tool.category == 'LLM').all()
    return render_template('tools.html', tools=tools, llms=llms)

@bp.route('/category/<category>')
def category(category):
    # TODO: Fetch tools by category
    tools = []
    return render_template('tools_category.html', category=category, tools=tools)

@bp.route('/tool/<int:tool_id>')
def tool(tool_id):
    # TODO: Fetch specific tool from database
    tool = Tool.query.get_or_404(tool_id)
    return render_template('tool_detail.html', tool=tool)

# Add a new route for comparing tools
@bp.route('/compare')
def compare():
    # TODO: Implement tool comparison functionality
    tool_ids = request.args.getlist('tool_id')
    tools = []  # Fetch tools based on tool_ids
    return render_template('tool_comparison.html', tools=tools)