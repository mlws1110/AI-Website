from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import Tool inside create_app to avoid circular import
    from app.models.tool import Tool
    
    admin = Admin(app, name='AI News Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(Tool, db.session))

    from app.routes import main, news, tools, modalities
    app.register_blueprint(main.bp)
    app.register_blueprint(news.bp)
    app.register_blueprint(tools.bp)
    app.register_blueprint(modalities.bp)

    # Error handling
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500  # Ensure a response is returned

    return app  # Ensure the app is returned