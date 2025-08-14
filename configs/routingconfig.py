#Blue Print for the routing configuration
from flask import Blueprint
from routers.routeexample import loginController
  
def  init_Blueprint(app):
    # Create a blueprint for the routing configuration
    # Import the route example module and register it with the blueprint
    app.register_blueprint(loginController, url_prefix="/usercontroller")
    #Add more blueprints as needed
    