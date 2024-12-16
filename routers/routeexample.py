from flask import Blueprint, jsonify, request
from model import commonresponsemodel as respm
from utils import commons as cv

loginController = Blueprint("logincontroller", __name__)


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


@loginController.route('/hi', methods=[cv.GET])

def sayhi():
  
    return "HI"


