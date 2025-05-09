import logging
import logging.config
from flask import Flask
from configs.checkingintro import LOGGING_CONFIG

class LogInstance:
    

    def __init__(self, app: Flask = None):
        # Apply the logging config
        logging.config.dictConfig(LOGGING_CONFIG)
        self.log = logging.getLogger("FlaskAppLogger")
        
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.logger.handlers = self.log.handlers
        app.logger.setLevel(self.log.level)
        self.log = app.logger

    def logger_info(self, message=None, file=None):
        self.log.info(f"{str(file)} : {message}" if file else message)

    def logger_error(self, message=None, file=None):
        self.log.error(f"{str(file)} : {message}" if file else message)

    def logger_warning(self, message=None, file=None):
        self.log.warning(f"{str(file)} : {message}" if file else message)
