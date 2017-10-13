#DEPRECATED
#Es la primera versión de lo que después pasé a Powershell (Buscador de IPs en linea.ps1)
#Este script toma un rango de IPs introducido por el usuario y verifica su estado, si responden a red las imprime en pantalla.
#Gastón Galarza, MDA-Tecnico 09/2017, github.com/gastonhz/Scripts

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
