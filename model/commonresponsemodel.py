from flask import jsonify


def createResponse(rescode, response):
    return jsonify(response.createDictionarie, rescode)


class CommonRequestModel:
    def __init__(self, message, code, data, stcodes=None):
        self.message = message
        self.code = code
        self.data = data
        self.stcode = stcodes

    def createDictionarie(self):
        responsd = {
            "message": self.message,
            "code": self.code,
            "data": self.data
        }
        return responsd

    def createDictionari_respo(self):
        responsd = {
            "message": self.message,
            "code": self.code,
            "data": self.data
        }
        return jsonify(responsd), self.stcode