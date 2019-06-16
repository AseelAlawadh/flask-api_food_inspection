from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
from flask_marshmallow import Marshmallow
from app.extenstions.logging import Logging

db = SQLAlchemy()

force_auto_coercion()
force_instant_defaults()

marshmallow = Marshmallow()

logging = Logging()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            db,
            marshmallow,
            logging
    ):
        extension.init_app(app)
