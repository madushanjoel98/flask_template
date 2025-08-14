from flask_cors import CORS
from utils.settingsreader import propReader
import datetime

##########################################
access_json=propReader()
nested_loging = f'{access_json["file_location"]}{access_json["appname"]}/log'
# Path to your requirements.txt file
LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        
        'formatters': {
            'detailed': {
                'format': '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            },
        },
        
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'detailed',
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'detailed',
                'filename': f'{nested_loging}/app-{str(datetime.date.today())}.log',
            },
        },

        'root': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }

def init_CORS(app):
    origins_array = propReader()["cross_orgins"]
    CORS(app, origins=origins_array)
    # flask_cors.cross_origin(
    #     methods=['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT'],
    #     headers=None,
    #     supports_credentials=False,
    #     max_age=None,
    #     send_wildcard=True,
    #     always_send=True,
    #     automatic_options=False
    #     )  