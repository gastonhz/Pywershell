#Este script borra archivos temporales en algunas rutas del sistema.
#Traducción a Powershell de Temporales.py
#github.com/gastonhz/Pywershell
"Limpiador de temporales"
""
$hostname=Read-Host -Prompt "Ingresar IP: "

$usuarios=Get-ChildItem -path \\$hostname\c$\Users\ -name

Remove-Item -path \\$hostname\c$\temp\* -force -recurse
"Eliminados los temporales de C:\Temp de $hostname"

Foreach ($user in $usuarios)
{
Remove-Item -path \\$hostname\c$\Users\$user\Appdata\Local\Temp\* -force -recurse
"Eliminados los temporales de Appdata\Local\Temp de $user"
Remove-Item -path \\$hostname\c$\Users\$user\Appdata\Local\Microsoft\Windows\INetCache\* -force -recurse
"Eliminados los temporales de Appdata\Local\Microsoft\Windows\INetCache de $user"
Remove-Item -path \\$hostname\c$\Users\$user\Appdata\LocalLow\Sun\Java\Deployment\Cache\* -force -recurse
"Eliminados los temporales de Appdata\LocalLow\Sun\Java\Deployment\Cache de $user"
}
    
"Finalizado. Algunos archivos pueden estar en uso y no haber sido borrados."
