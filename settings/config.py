from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(BASEDIR, '.env')

load_dotenv(path)

def load_env_config():
    return {
        'server': os.getenv("DATABASE_SERVER"),
        'database': os.getenv("DATABASE"),
        'database_user': os.getenv("DATABASE_USERNAME"),
        'database_pass': os.getenv("DATABASE_PASSWORD"),
        'cleardb_database_url': os.getenv("CLEARDB_DATABASE_URL"),
        'database_string': os.getenv("DATABASE_STRING"),
        'secret_key': os.getenv("ACCESS_SECRET_KEY"),
        'password_salt': os.getenv("ACCESS_SALT"),
        'mail_server': os.getenv('MAIL_SERVER'),
        'mail_port': os.getenv('MAIL_PORT'),
        'mail_use_tls': os.getenv('MAIL_USE_TLS'),
        'mail_use_ssl': os.getenv('MAIL_USE_SSL'),
        'mail_username': os.getenv('MAIL_USERNAME'),
        'mail_password': os.getenv('MAIL_PASSWORD'),
        'vanso_username': os.getenv('VANSO_USERNAME'),
        'vanso_password': os.getenv('VANSO_PASSWORD'),
        'vanso_url': os.getenv('VANSO_URL'),
        'vanso_sender_id': os.getenv('VANSO_SENDER_ID'),
    }

