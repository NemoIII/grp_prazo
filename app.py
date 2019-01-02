from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app(config=None):
	app = Flask(__name__)
	
	if config is not None:
		app.config.from_object(config)
	
	db.init_app(app)
	
	# from user.views import app_page
	# app.register_blueprint(app_page, url_prefix="/")
	
	return app