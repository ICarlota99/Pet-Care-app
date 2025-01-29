from flask import Flask
from .home_routes import home_bp
from .auth_routes import auth_bp
from .pet_routes import pet_bp
from .gallery_routes import gallery_bp
from .logs_routes import logs_bp
from .trackers_routes import trackers_bp

def register_routes(app: Flask):
    """Register all Blueprints with the Flask app."""
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(pet_bp)
    app.register_blueprint(gallery_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(trackers_bp)
