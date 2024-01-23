from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import psycopg2
import os

import routes
from log_config import setup_logstash_log
import model

load_dotenv

def create_app():
    try:
        app = Flask(__name__)
        environ = os.getenv("FLASK_CONFIG") if os.getenv("FLASK_CONFIG") != None else "config.DevelopmentConfig"

        app.config.from_object(environ)
        
        if "PrdConfig" in environ:
            setup_logstash_log(app)

        model.init_app(app)
        migrate = Migrate()
        from model import db
        migrate.init_app(app, db)
        routes.init_app(app)

        CORS(app)

        from handler import ErrorHandler
        
        app.register_error_handler(500, ErrorHandler.handle_server_error)
        app.register_error_handler(401, ErrorHandler.handle_user_error)
        app.register_error_handler(403, ErrorHandler.handle_user_error)

        return app
    except psycopg2.OperationalError as e:
        app.logger.error(e)
    except Exception as e:
        app.logger.error(e, exc_info=True)