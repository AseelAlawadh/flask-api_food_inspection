def init_app(app, **kwargs):
    from app.analysis import route  # pylint: disable=unused-variable
    app.register_blueprint(route.api)
