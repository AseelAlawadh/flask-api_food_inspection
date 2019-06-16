from flask import jsonify, Blueprint

api = Blueprint("food", __name__, url_prefix='/food')


@api.route('/', methods=['GET'])
def create():
    result = {
        "message": "hi this response from /food/"
    }
    return jsonify(result)
