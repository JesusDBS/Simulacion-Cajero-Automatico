from db_conection import DB

db = DB()

# create tables
db.my_cursor.execute('''

    CREATE TABLE USUARIOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE VARCHAR(40) NOT NULL,
    APELLIDO VARCHAR(40) NOT NULL,
    CI VARCHAR(10) UNIQUE NOT NULL, 
    NUMERO_DE_TARJETA VARCHAR(19) UNIQUE NOT NULL,
    CLAVE VARCHAR(10) NOT NULL,
    SALDO INTEGER)
''')

# inserting data
usuarios = [

    ("Fulano", "Martínez", "11111111", "XXXXXXXXXXXXXXXXXXX", "XXXX", 80),
    ("Sutano", "Martínez", "22222222", "YYYYYYYYYYYYYYYYYYY", "YYYY", 40),
    ("Perensejo", "Pedráz", "33333333", "ZZZZZZZZZZZZZZZZZZZ", "ZZZZ", 180),
]

db.my_cursor.executemany(
    "INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?,?)", usuarios)

db.commit()
db.close()
