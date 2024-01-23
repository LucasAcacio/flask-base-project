from flask import Blueprint
from flask_restful import Api

bp = Blueprint("restapi", __name__, url_prefix="/myflask/v1")
api = Api(bp)

def init_app(app):
    """
        Função que inicia as rotas no flask
    """
    from routes.healthcheck import healthcheck_bp
    
    bp.register_blueprint(healthcheck_bp)
    app.register_blueprint(bp)