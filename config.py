# pylint: disable=too-few-public-methods

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LDAP_SERVER = os.getenv("LDAP_SERVER")
    LDAP_USER_BASE_DN = os.getenv("LDAP_USER_BASE_DN")
    LDAP_ENABLE_TLS = os.getenv("LDAP_ENABLE_TLS", "no").lower() == "yes"
    LDAP_CA_PATH = os.getenv("LDAP_CA_PATH")
    LDAP_BINDER = os.getenv("LDAP_BINDER")
    LDAP_BINDER_CREDENTIAL = os.getenv("LDAP_BINDER_CREDENTIAL")

    ADMIN_GROUPS = os.getenv("ADMIN_GROUPS")

    DEBUG = False
    ALLOW_CORS = False

class DevelopmentConfig(Config):
    DEBUG = True
    ALLOW_CORS = True

class ProductionConfig(Config):
    DEBUG = False
    ALLOW_CORS = False

def get_runtime_config():
    return os.getenv("RUNTIME_CONFIG", "Development")
