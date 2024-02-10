import pandas as pd
import os
import re

path = 'Activities/Practice 2/Directorio.csv'

regexp_phone = re.compile(r'^\d{10}$')
regexp_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
regexp_name = re.compile(r'^[a-zA-Z ]+$')

while True:
        while True:
                name = input("Ingrese su nombre: ")
                if regexp_name.match(name):
                        break
                else:
                        print("Nombre no valido")
                        
        while True:
                phone = input("Ingrese su numero\nSolo 10 digitos: ")
                if regexp_phone.match(phone):
                        break
                else:
                        print("Numero no valido")

        while True:
                email = input("Ingrese su email: ")
                if regexp_email.match(email):
                        break
                else:
                        print("Correo incorrecto")

        address = input("Ingrese su domicilio: ")
        
        if os.path.exists(path):
                existing_data = pd.read_csv(path)

                new_data = pd.DataFrame([
                        [name, phone, email, address]
                        ],columns=["Nombre", "Telefono", "Correo", "Domicilio"])
                        
                update_data = pd.concat([existing_data, new_data], ignore_index=True)
                update_data.to_csv(path, index=False)
        else:
                directory = pd.DataFrame([
                        [name, phone, email, address]
                        ],columns=["Nombre", "Telefono", "Correo", "Domicilio"])
                                
                directory.to_csv(path, index=False)
        break