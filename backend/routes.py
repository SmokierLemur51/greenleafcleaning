from quart import Quart, render_template


async def configure_core_routes(app: Quart) -> None:
    @app.route("/")
    async def index():
        elements = {'title': 'Success'}
        return await render_template("index.html", elements=elements)

    @app.route("/services")
    async def services():
        elements = {}
        return await render_template("services.html", elements=elements)


async def configure_test_routes(app: Quart) -> None:

    @app.route("/schema/create")
    async def create_tables():
        pass

