from flask_jwt_extended import create_access_token, create_refresh_token
from utils.dbMethods import DBOperator
from datetime import timedelta

dbp = DBOperator()


def getAllUsers():
    return dbp.read("SELECT * FROM plc_new.officer;")


def getAllUsersByEPF(epfno):
    query = f'SELECT * FROM plc_new.officer where EpfNo="{epfno}";'
    data = dbp.read(query)
    if len(data) == 0:
        raise Exception("no Data")
    return data


def getAllUsersByName(name):
    query = f'SELECT * FROM plc_new.officer where Name or calling_name like "%{name}%"'
    data = dbp.read(query)
    if len(data) == 0:
        raise Exception("no Data")
    return data


def login(username, password):
    access_token = None
    query = f'SELECT * FROM tut.users where name="{username}" and password="{password}";'
    data = dbp.read(query)
    if len(data) == 0:
        raise Exception("Fail Login")
    # d
    else:
        print(data[0])
        user = data[0]
        expires = timedelta(hours=1)
        access_token = create_access_token(identity=user, expires_delta=expires)
        refresh_token = create_refresh_token(identity=user)
        toke = {"user": user, "token": access_token, "expiedin": expires.seconds, "refreshtoken": refresh_token}
    return toke


def genrateToken(userid: int, token: str):
    query = f"INSERT INTO token (token, userid,date) VALUES ('{token}',{userid},NOW())"

    data = dbp.inserts(query=query)

    return data