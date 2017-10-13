#Este script simplemente imprime las carpetas que se encuentran dentro de C:\Users.
#La idea es pasarlo a Powershell.
#Gastón Galarza, MDA-Tecnico 09/2017, github.com/gastonhz/Scripts
import os
import re
hostname=input("Ingresar host: ")
ruta=r"\\"+hostname+r"\c$"+r"\Users"+r"\\"
users=os.listdir(ruta)
print("Usuarios encontrados:")
print(users)
