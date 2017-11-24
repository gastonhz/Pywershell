#Este script simplemente imprime las carpetas que se encuentran dentro de C:\Users.
#La idea es pasarlo a Powershell.
#github.com/gastonhz/Pywershell
import os
import re
hostname=input("Ingresar host: ")
ruta=r"\\"+hostname+r"\c$"+r"\Users"+r"\\"
users=os.listdir(ruta)
print("Usuarios encontrados:")
print(users)
