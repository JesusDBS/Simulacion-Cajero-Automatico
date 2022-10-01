from funciones_cajero import Cajero

cajero = Cajero()

if __name__ == "__main__":
    
    print("Welcome, please insert your data\n")
    cajero.get_data()

    while True:
        cajero.options()
        cajero.acctions()
        option = cajero.salir()

        if option is None:
            print("Hasta pronto!")
            break
