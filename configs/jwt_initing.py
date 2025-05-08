from flask_jwt_extended import JWTManager
from utils.settingsreader import propReader


def init_jwt(app):
    '''Initialize JWT for the Flask app. use it in the main app file.'''
    if propReader()["secure"]:
        app.config['SECRET_KEY'] = propReader()["secret_key"]  # Change this to a secure secret key
        JWTManager(app=app)
    pass


def jwt_identity(payload):
    '''JWT identity function to extract user identity from the JWT payload'''
    user_id = payload['identity']
    # Example identity logic (replace with your own)
    return {'user_id': user_id}


def authenticateUser(username, password):
    '''JWT authentication function to verify user credentials  please replace with your own logic'''
    # Example authentication logic (replace with your own)
    if username == 'admin' and password == 'password':
        return {'username': username}
    return None
