import os
import re

ipmaster=input("Ingresar IP con formato 10.xxx.xxx.:")
suma=0
listaips=[]
for ip in range(9,30):
    strip=str(ip)
    hostfound=os.system("ping -n 2 -w 500 "+ipmaster+strip)
    #se podria agregar que busque en un rango introducido por el usuario
    #para que el script sea universal
    if hostfound==0:
        print(ipmaster+strip)
        listaips.append(ipmaster+strip)
        suma=suma+1
print("Finalizado,", suma, " host disponibles")

##hostname=input("Ingresar host: ")
##users=os.listdir(ruta)
##print("Usuarios encontrados:")
##print(users)
##print()
##print("Limpiando cola de impresión...")
##
##for item in listaips:
##    Cprint="\\"+item+"\c$"+"\Windows"+"\System32"+"\spool"+"\PRINTERS"+"\*"
##    os.system("sc "+r"\\"+item+" stop spooler")
##    os.system("del /Q /F /S "+Cprint)
##    os.system("sc \\"+item+" start spooler")
##
##print("Finalizado. Algunos archivos pueden estar en uso y no haber sido borrados.")
##
