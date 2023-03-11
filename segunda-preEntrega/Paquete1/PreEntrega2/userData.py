class UserData:

        def __init__(self, name, lastname, age, mail):
                self.name = name
                self.lastname = lastname
                self.age = age
                self.mail = mail
        
        def __str__(self):
                return f"Ingrese nuevamente con usuario y contraseña para confirmar registro de cliente \n :{self.name}, {self.lastname}, Edad:{self.age}, Correo:{self.mail}"
        
        def registerUser(self, userdb):
                userdb["name"] = self.name
                userdb["lastname"] = self.lastname
                userdb["age"] = self.age
                userdb["mail"] = self.mail     
                return userdb
        
        def paswStructure(self, pasw):
                points = 0
                for x in range(len(pasw)):
                        if pasw[x].isupper() == True:
                                points += 1
                        elif pasw[x].isalnum() == False:
                                points += 1
                        elif pasw[x].isnumeric() == True:
                                points += 1
                return points
