from flask import Flask
from routers.routeexample import loginController


app = Flask(__name__)

app.register_blueprint(loginController, url_prefix="/usercontroller")


if __name__ == '__main__':
    # init_db()
    # print(uuid.uuid4())
    # connecDB.get_connection().connect()
    app.run(debug=True)