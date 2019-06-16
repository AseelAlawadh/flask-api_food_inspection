def init_app(app, **kwargs):
    from app.food import route  # pylint: disable=unused-variable
    app.register_blueprint(route.api)
