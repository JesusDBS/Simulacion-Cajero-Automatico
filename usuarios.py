from db_conection import DB

db = DB()


class Usuario():

    def __init__(self, numero_de_tarjeta, clave):

        self.numero_de_tarjeta = numero_de_tarjeta
        self.clave = clave
        self.id = None
        self.FirstName = None
        self.LastName = None
        self.ci = None
        self.saldo = None

        self.deposito = None

    def auth(self):

        values = (self.numero_de_tarjeta, self.clave)
        user = db.my_cursor.execute(
            "SELECT * FROM USUARIOS WHERE NUMERO_DE_TARJETA=? AND CLAVE=?", values)

        user = list(user)

        if user:

            self.id = user[0][0]
            self.FirstName = user[0][1]
            self.LastName = user[0][2]
            self.ci = user[0][3]
            self.saldo = user[0][6]

            print("Welcome " + self.FirstName + " " + self.LastName + "!\n")

        else:
            print("Password or card number invalid\n")

    def check_my_balance(self):

        print("Your balance is " + str(self.saldo) + " $.\n")

    def movimientos(self, monto, movimiento):

        if int(movimiento) == 1:
            monto = self.saldo - float(monto)
        else:
            monto = self.saldo + float(monto)

        values = (monto, self.id)
        db.my_cursor.execute("UPDATE USUARIOS SET SALDO=? WHERE ID=?", values)

        new_saldo = db.my_cursor.execute(
            "SELECT SALDO FROM USUARIOS WHERE ID=?", (self.id,))
        new_saldo = list(new_saldo)

        self.saldo = new_saldo[0][0]

        db.commit()

        self.check_my_balance()

    def salir(self):
        db.close()
