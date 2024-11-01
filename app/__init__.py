from flask import Flask
from .controllers import user_bp
from .modules import *

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f"config.{config_name.capitalize()}Config")
    app.ldap_conn = ldap_conn_establish(app.config)

    app.register_blueprint(user_bp)

    return app
