import os
import re
hostname=input("Ingresar host: ")
Ctemp=r"\\"+hostname+r"\c$"+r"\Temp"+r"\\*"
ruta=r"\\"+hostname+r"\c$"+r"\Users"+r"\\"
users=os.listdir(ruta)
print("Usuarios encontrados:")
print(users)
