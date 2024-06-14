from .factory import create_app
import uvicorn


def run() -> None:
    app = create_app()
    # uvicorn.run(app, host="0.0.0.0", port=5000)
    app.run()