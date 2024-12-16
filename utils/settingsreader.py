import json

path = "./setting.json"
def propReader():
    data = None
    with open(path) as json_file:
        data = json.load(json_file)
    # print(data)
    return data


def isSeucre():
    return propReader()["secure"]

