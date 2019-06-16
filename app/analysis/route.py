from flask import jsonify, Blueprint

api = Blueprint("analysis", __name__, url_prefix='/analysis')


@api.route('/', methods=['GET'])
def create():
    result = {
        "message": "hi this response from /analysis/"
    }
    return jsonify(result)
