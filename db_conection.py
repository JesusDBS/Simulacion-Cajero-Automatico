import sqlite3


class DB:
    def __init__(self):
        self.__ruta = 'usuarios.db'
        self.my_co = sqlite3.connect(self.__ruta)
        self.my_cursor = self.my_co.cursor()

    def commit(self):
        self.my_co.commit()

    def close(self):
        self.my_co.close()
