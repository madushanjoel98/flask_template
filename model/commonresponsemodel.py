from flask import jsonify

def create_response(response_obj):
    """Creates a JSON response from the CommonRequestModel instance."""
    return jsonify(response_obj.to_dict()), response_obj.stcode
class CommonRequestModel:
    def __init__(self, message, code, data=None, stcode=200):
        self.message = message
        self.code = code
        self.data = data
        self.stcode = stcode

    def to_dict(self):
        """Convert response object to dictionary."""
        return {
            "message": self.message,
            "code": self.code,
            "data": self.data
        }
