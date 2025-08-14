from flask import Blueprint, jsonify, request
from model import commonresponsemodel as respm
from utils import commons as cv
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended.utils import create_access_token, get_jwt_identity
from configs.jwt_initing import authenticateUser
from utils.logger import LogInstance


loginController = Blueprint("logincontroller", __name__)

logg= LogInstance()

@loginController.route('/signup', methods=["POST"])
def signupUser():
    data = request.get_json()
    res = None
    stCode = cv.OK
    try:
       res = respm.CommonRequestModel(message="", data=None, code=1)
    
    except Exception as e:
        stCode = cv.BAD_REQUEST
        res = respm.CommonRequestModel(message=f"Failed {e}", data=None, code=2)

    return jsonify(res.createDictionarie()), stCode

@loginController.route("/")
def index():
    logg.logger_info(message="hello starter", file="logincontroller")
    return "hello"

@loginController.route("/login", methods=["POST"])
def login():

    data = request.get_json()
    if(authenticateUser(data.get("username"), data.get("password"))== None):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=data.get("username"), expires_delta=None)
    return jsonify(access_token=access_token )


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@loginController.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

