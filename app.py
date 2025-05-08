from flask import Flask
from configs.routingconfig import init_Blueprint
from configs.jwt_initing import jwt_identity, init_jwt

app = Flask(__name__)
init_jwt(app)  # Initialize JWT for the Flask app
init_Blueprint(app);

if __name__ == '__main__':
    # init_db()
    # print(uuid.uuid4())
    # connecDB.get_connection().connect()
    app.run(debug=True, port=5000)
