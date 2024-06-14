from dotenv import load_dotenv
from quart import Quart


load_dotenv()


def create_app(**config_overrides):
	app = Quart(__name__, static_url_path='/static')
	
	# env config
	app.config.from_pyfile("settings.py")
	
	# config obj
	from .config import Config
	app.config.from_object(Config)
	
	# config overrides
	app.config.update(config_overrides)

	from .db import db
	db.init_app(app)
	
	from .routes import configure_core_routes
	configure_core_routes(app=app)
	
	return app

