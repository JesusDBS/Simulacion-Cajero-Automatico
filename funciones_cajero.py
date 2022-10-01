from usuarios import Usuario


class Cajero():

    def get_data(self):
        while True:
            num_tarjeta = input("Introduce el número de tu tarjeta: ")
            clave = input("Introducte tu clave: ")
            print('')

            self.usuario = Usuario(num_tarjeta, clave)

            self.usuario.auth()
            print('')

            if self.usuario.id is not None:
                break

    def check_options(self, LimInf, LimSup):
        option = input("Ingrese el número de la acción que desea realizar: ")
        print('')

        if option.isdigit() is True:
            if (int(option) <= LimSup and int(option) >= LimInf):
                return option

            else:
                print(
                    "Usted debe ingresar uno de los números que aparecen en pantalla.\n")
        else:
            print("Usted debe ingresar uno de los números que aparecen en pantalla.\n")

    def options(self):
        while True:
            print("Qué desea realizar?\n")
            print("1. Retiro\n")
            print("2. Depósito\n")
            print("3. Consulta\n")

            self.option = self.check_options(1, 3)

            if self.option:
                break

    def check_monto(self, accion):
        while True:
            self.monto = input(
                "Introduzca el monto que desea " + accion + " : ")
            print("")
            if self.monto.isdigit():
                break
            else:
                print("El monto que ha ingresado no es válido.")

        return self.monto

    def acctions(self):
        if int(self.option) == 1:

            while True:
                retiro = "retirar"
                monto = self.check_monto(retiro)
                if int(monto) >= self.usuario.saldo:
                    print("El monto debe ser menor a tu saldo disponible")
                else:
                    self.usuario.movimientos(monto, self.option)
                    break

        elif int(self.option) == 2:
            deposito = "depositar"
            monto = self.check_monto(deposito)
            self.usuario.movimientos(monto, self.option)

        else:
            self.usuario.check_my_balance()

    def salir(self):
        while True:
            print("Gracias por usar nuestro servicio! Desea continuar?\n")
            print("1. No, deseo salir\n")
            print("2. deseo continuar\n")

            self.option = self.check_options(1, 2)

            if self.option:
                if int(self.option) == 1:
                    self.usuario.salir
                    break

            return self.option
