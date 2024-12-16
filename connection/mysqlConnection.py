import  mysql.connector
from mysql.connector import Error
from utils.settingsreader as reas


class MYConnection:
    dbi = propReader()['database']

    def __init__(self):
        self.mydb = None
        self.connect()

    def connect(self):
        try:
            self.mydb = mysql.connect(
                host=self.dbi["host"],
                user=self.dbi["username"],
                password=self.dbi["password"],
                database=self.dbi["db"]
            )
            if self.mydb.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.mydb = None

    def get_connection(self):
        if self.mydb is None or not self.mydb.is_connected():
            print("Reconnecting to MySQL database")
            self.connect()
        if self.mydb is not None and self.mydb.is_connected():
            return self.mydb
        else:
            raise Exception("Connection Failed")

