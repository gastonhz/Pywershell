#Este script borra archivos temporales en algunas rutas del sistema.
#github.com/gastonhz/Pywershell
import os
import re
hostname=input("Ingresar IP: ")
Ctemp=r"\\"+hostname+r"\c$"+r"\Temp"+r"\\*"
ruta=r"\\"+hostname+r"\c$"+r"\Users"+r"\\"
users=os.listdir(ruta)
print("Usuarios encontrados:")
print(users)
print()
print("Limpiando...")

os.system("del /Q /F /S "+Ctemp)

for item in users:
    os.system("del /Q /F /S "+ruta+item+r"\AppData"+r"\local"+r"\temp"+r"\*")
    os.system("del /Q /F /S "+ruta+item+r"\AppData"+r"\local"+r"\Microsoft"+r"\Windows"+r"\INetCache"+r"\*")
    os.system("del /Q /F /S "+ruta+item+r"\AppData"+r"\local"+r"\Microsoft"+r"\Windows"+r"\INetCookies"+r"\*")
    os.system("del /Q /F /S "+ruta+item+r"\AppData"+r"\LocalLow"+r"\Sun"+r"\Java"+r"\Deployment"+r"\Cache"+r"\*")
    

print("Finalizado. Algunos archivos pueden estar en uso y no haber sido borrados.")
