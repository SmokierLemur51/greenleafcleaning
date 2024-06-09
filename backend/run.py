from quart import Quart
from quart_db import QuartDB

from routes import configure_core_routes

app = Quart(__name__, static_url_path="/static")
db = QuartDB(app, url="sqlite:///instance/aio_testing.db")

# routes
configure_core_routes(app)

# Send it to the moon
app.run(debug=True)