import json
from PreEntrega2.userData import UserData


#Registro y/o validacion de usuario
def login(db):
    done = "Y"
    while done == 'Y':

        user = input("Ingrese su usuario o cree uno nuevo\n")
        pasw = input("Ingrese su contraseña \n")
        print(db.keys())
        
        if user in db.keys():
            if pasw == db[user]['pasw']:
                print("Ingreso correcto")
                break
            else:
                print("Usuario o contraseña incorrecta \n")
                continue
        
        else:
            dbuser = dict()
            points = 0
            while points == 0:
                checkPasw = UserData(None, None, None, None)
                points = checkPasw.paswStructure(pasw)
                if points > 3:
                    dbuser['pasw'] = pasw
                    db[user] = dbuser
                    print("Registro correcto\n")
                else:
                    print("La contraseña debe contener un numero, una mayuscula y un caracter especial")
                    pasw = input("Ingrese su contraseña \n")
    

            #Registrar usuario en base de datos
            name = input("Nombre: \n")
            lastname = input("Apellido: \n")
            age = input("Edad: \n")
            mail = input("Correo: \n")

            newUser = UserData(name, lastname, age, mail)
            db[user] = newUser.registerUser(userdb = dbuser)
            print(newUser)
        
#Almacenar informacion
def db_file(db):
    f = open('base-datos.json','x')
    f.write(json.dumps(db))

#Mostrar informacion 
def read_db(db):
    for k, v in db.items():
        print(k, v)