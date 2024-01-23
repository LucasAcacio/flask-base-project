from flask import Blueprint, Response, make_response, jsonify

healthcheck_bp = Blueprint('healthcheck', __name__, url_prefix="/healthcheck")

@healthcheck_bp.route('', methods=['GET'])
def get() -> Response:
    '''
        Do your thing ;D
    '''
    all_good = True
    response = {}
    if all_good:
        response = {
            "status": "healthy",
            "message": "all good!"
        }

    else:
        response = {
            "status": "unhealthy",
            "message": "oof"
        }
         
    return make_response(jsonify(response), 200)