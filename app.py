from flask import Flask
from configs.routingconfig import init_Blueprint
from configs.jwt_initing import jwt_identity, init_jwt
from flask.templating import render_template
from configs.checkingintro import init_CORS
from configs.setupConfig import setUpingFolders

app = Flask(__name__)
#Initializer
init_jwt(app)  # Initialize JWT for the Flask app
init_Blueprint(app);
init_CORS(app)

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == '__main__':
    # init_db()
    # print(uuid.uuid4())
    # connecDB.get_connection().connect()
    setUpingFolders()
    app.run(debug=True, port=5000)
